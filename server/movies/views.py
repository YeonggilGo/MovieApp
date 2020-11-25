from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from django.db.models import Q

import operator
import requests
import random
from itertools import combinations as coms
from functools import reduce

from .models import Movie, Genre, Review
from .serializers import MovieSerializer, ReviewSerializer


class URLMaker:
    key = "26098e52c62da6e76a55e7bd6d69635e"

    def __init__(self):
        self.url = ""

    def getMovies(self, i):
        return f'https://api.themoviedb.org/3/movie/popular?api_key={self.key}&language=ko-KR&page={i}'

    def getGenres(self):
        return f'https://api.themoviedb.org/3/genre/movie/list?api_key={self.key}&language=ko-KR'

    def searchMovie(self, word):
        return f'https://api.themoviedb.org/3/search/movie?api_key={self.key}&query={word}&page=1'

    def recommendMovie(self, id):
        return f'https://api.themoviedb.org/3/movie/{id}/recommendations?api_key={self.key}&language=ko-KR&page=1'


def add_new_movie(movie):
    genre_url = URLMaker()
    genre_list = requests.get(genre_url.getGenres()).json()
    genre_dict = {x['id']: x['name'] for x in genre_list['genres']}

    new_movie = Movie(
        title=movie.get('title'),
        origin_title=movie.get('original_title'),
        poster_path=movie.get('poster_path'),
        overview=movie.get('overview'),
        backdrop_path=movie.get('backdrop_path'),
        popularity=movie.get('popularity'),
        vote_count=movie.get('vote_count'),
        video=movie.get('video'),
        adult=movie.get('adult'),
        origin_language=movie.get('original_language'),
        vote_average=movie.get('vote_average'),
        release_date=movie.get('release_date')
    )
    new_movie.save()
    for genre_id in movie['genre_ids']:
        if not Genre.objects.filter(id=genre_id).exists():
            cur_genre = Genre(
                id=genre_id, title=genre_dict[genre_id])
            cur_genre.save()
        new_movie.genres.add(genre_id)
    res = Movie.objects.filter(pk=new_movie.pk)
    return res


@api_view(['GET'])
def movie_list(request):
    if not Movie.objects.all().exists():
        url = URLMaker()
        for i in range(1, 51):
            movies = requests.get(url.getMovies(i)).json()['results']
            for temp in movies:
                add_new_movie(temp)
    movies = Movie.objects.all()
    serializer = MovieSerializer(movies, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def popular_movies(request):
    movies = Movie.objects.order_by('popularity')
    pks = random.sample([movie.id for idx, movie in enumerate(movies) if idx < 40], 20)
    movies = movies.filter(pk__in=pks)
    serializer = MovieSerializer(movies, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def genre_movies(request, genre_id, ):
    movies = Movie.objects.filter(genres=genre_id)
    serializer = MovieSerializer(movies, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def movie_detail(request, movie_pk):
    movie = Movie.objects.get(pk=movie_pk)
    serializer = MovieSerializer(movie)
    return Response(serializer.data)


@api_view(["GET"])
def recommend_movies(request):
    movies = Movie.objects.none()
    if request.user.is_authenticated:
        user_pk = request.user.pk
        user = get_object_or_404(get_user_model(), pk=user_pk)
        like_movies = user.like_movies.all()
        if like_movies.exists():
            prefer_dict = {}
            for movie in like_movies:
                for genre in movie.genres.all():
                    if genre.id in prefer_dict:
                        prefer_dict[genre.id] += 1
                    else:
                        prefer_dict[genre.id] = 1

            user_prefer = {}
            for key, value in prefer_dict.items():
                if value in user_prefer:
                    user_prefer[value].append(key)
                else:
                    user_prefer[value] = [key]
            keys = sorted(list(user_prefer.keys()), reverse=True)

            # case 1 : Recommend movie using TMDB api
            recommendURL = URLMaker()
            like_movie_ids = [m.id for m in like_movies]
            for id in like_movie_ids:
                data = request.get(recommendURL.recommendMovie(id)).json()['results']
                for movie in data:
                    if Movie.objects.get(title=movie['title']).exists():
                        movies |= Movie.objects.filter(title=movie['title'])
                    else:
                        new_movie = add_new_movie(movie)
                        movies |= new_movie

            # case 2 : Recommend movie by genre in DB
            for i in range(0, len(keys)):
                temp_genres = reduce(lambda x, m: x + m, [user_prefer[keys[j]] for j in range(i + 1)], [])
                for j in range(len(temp_genres), 0, -1):
                    for com in coms(temp_genres, j):
                        temp_movies = Movie.objects.all()
                        for cur_genre in com:
                            temp_movies = temp_movies.filter(genres=cur_genre)
                        movies |= temp_movies
                    if len(movies) >= 36:
                        pks = random.sample([x.id for x in movies], 12)
                        temp_movies = movies.filter(id__in=pks).order_by('?')
                        serializer = MovieSerializer(temp_movies, many=True)
                        return Response(serializer.data)

    if len(movies) < 12:
        pks = random.sample(range(1, 1001), 12 - len(movies))
        temp_movies = Movie.objects.filter(id__in=pks)
        movies |= temp_movies
        movies = movies.order_by('?')
    serializer = MovieSerializer(movies, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def search_movies(request):
    target = request.GET.get('word')
    target_words = target.split()
    target_words = [word.strip() for word in target_words]
    movies = Movie.objects.none()

    # case 1 : From TMDB, using search api
    searchURL = URLMaker()
    for word in target_words:
        res = requests.get(searchURL.searchMovie(word)).json()['results']
        for movie in res:
            if Movie.objects.filter(title=movie['title']).exists():
                movies |= Movie.objects.filter(title=movie['title'])
            else:
                new_movie = add_new_movie(movie)
                movies |= new_movie

    # case 2 : search word in DB
    for i in range(len(target_words), 0, -1):
        for com in coms(target_words, i):
            movies |= Movie.objects.filter(
                reduce(operator.and_, (Q(title__contains=x) for x in com)) |
                reduce(operator.and_, (Q(origin_title__contains=x) for x in com)) |
                reduce(operator.and_, (Q(overview=x) for x in com)))
    if len(movies) == 0:
        return Response({'error': 'Not fount'}, status=status.HTTP_404_NOT_FOUND)
    serializer = MovieSerializer(movies, many=True)
    serializer.sort()
    return Response(serializer.data)


@api_view(['POST'])
def movie_like(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    movie.save()
    user = get_object_or_404(get_user_model(), pk=request.user.id)
    if movie.like_users.filter(id=request.user.id).exists():
        movie.like_users.remove(user)
        liked = False
    else:
        movie.like_users.add(user)
        liked = True

    like_status = {
        'liked': liked,
        'like_count': movie.like_users.count(),
    }
    return Response(like_status)


@api_view(['POST'])
def review_list_create(request, movie_pk):
    movie = get_object_or_404(Review, pk=movie_pk)
    if request.method == 'POST':
        review = Review.objects.create(
            movie=movie,
            user=request.user,
            content=request.data.content,
            username=request.user.username,
            score=request.data.score
        )
        serializer = ReviewSerializer(review)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
    else:
        reviews = Review.objects.filter(movie=movie_pk)
        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data)


@api_view(['POST'])
def review_update_delete(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)

    if request.user != review.user:
        return Response({'error': 'Not available'}, status=status.HTTP_401_UNAUTHORIZED)

    if request.method == 'DELETE':
        review.delete()
        return Response({'id': review_pk})
    elif request.method == 'GET':
        serializer = ReviewSerializer(review)
        return Response(serializer.data)
    else:
        review.content = request.data.content
        review.score = request.data.score
        serializer = ReviewSerializer(review)
        serializer.save()
        return Response(serializer.data)
