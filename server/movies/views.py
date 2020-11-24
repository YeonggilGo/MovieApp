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

from .models import Movie, Genre
from .serializers import MovieSerializer


class URLMaker:
    key = "26098e52c62da6e76a55e7bd6d69635e"

    def __init__(self):
        self.url = ""

    def getMovies(self, i):
        return f'https://api.themoviedb.org/3/movie/popular?api_key={self.key}&language=ko-KR&page={i}'

    def getGenres(self):
        return f'https://api.themoviedb.org/3/genre/movie/list?api_key={self.key}&language=ko-KR'


@api_view(['GET'])
def movie_list(request):
    if not Movie.objects.all().exists():
        url = URLMaker()
        genre_url = URLMaker()
        genre_list = requests.get(genre_url.getGenres()).json()
        genre_dict = {x['id']: x['name'] for x in genre_list['genres']}
        for i in range(1, 51):
            movies = requests.get(url.getMovies(i)).json()['results']
            for temp in movies:
                new_movie = Movie(
                    title=temp.get('title'),
                    origin_title=temp.get('original_title'),
                    poster_path=temp.get('poster_path'),
                    overview=temp.get('overview'),
                    backdrop_path=temp.get('backdrop_path'),
                    popularity=temp.get('popularity'),
                    vote_count=temp.get('vote_count'),
                    video=temp.get('video'),
                    adult=temp.get('adult'),
                    origin_language=temp.get('original_language'),
                    vote_average=temp.get('vote_average'),
                    release_date=temp.get('release_date')
                )
                new_movie.save()
                for genre_id in temp['genre_ids']:
                    if not Genre.objects.filter(id=genre_id).exists():
                        cur_genre = Genre(
                            id=genre_id, title=genre_dict[genre_id])
                        cur_genre.save()
                    new_movie.genres.add(genre_id)

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
def genre_movies(request, genre_id,):
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
            if user_prefer:
                for i in range(0, len(keys)):
                    temp_genres = reduce(lambda x, m: x + m, [user_prefer[keys[j]] for j in range(i + 1)], [])
                    for j in range(len(temp_genres), 0, -1):
                        for com in coms(temp_genres, j):
                            temp_movies = Movie.objects.all()
                            for cur_genre in com:
                                temp_movies = temp_movies.filter(genres=cur_genre)
                            movies |= temp_movies
                        if len(movies) >= 24:
                            pks = random.sample([x.id for x in movies], 12)
                            temp_movies = movies.filter(id__in=pks).order_by('?')
                            serializer = MovieSerializer(temp_movies, many=True)
                            return Response(serializer.data)

    pks = random.sample(range(2467, 3467), 12 - len(movies))
    temp_movies = Movie.objects.filter(id__in=pks)
    movies |= temp_movies
    movies = movies.order_by('?')
    serializer = MovieSerializer(movies, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def search_movies(request):
    target = request.data['word']
    target_words = target.split()
    target_words = [word.strip() for word in target_words]
    movie = Movie.objects.none()
    for i in range(len(target_words), 0, -1):
        for com in coms(target_words, i):
            movie |= Movie.objects.filter(reduce(operator.and_, (Q(title__contains=x) for x in com)))
            movie |= Movie.objects.filter(reduce(operator.and_, (Q(origin_title__contains=x) for x in com)))
    if len(movie) == 0:
        return Response({'error': 'Not fount'}, status=status.HTTP_404_NOT_FOUND)
    serializer = MovieSerializer(movie, many=True)
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
