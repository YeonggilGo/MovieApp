from rest_framework.response import Response
from rest_framework.decorators import api_view


import requests
import random
from itertools import combinations as coms
from django.db.models import Q

from .models import Movie, Prefer, Genre
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
                    title=temp['title'],
                    origin_title=temp['original_title'],
                    poster_path=temp['poster_path'],
                    overview=temp['overview'],
                    backdrop_path=temp['backdrop_path'],
                )
                new_movie.save()
                for genre_id in temp['genre_ids']:
                    if not Genre.objects.filter(id=genre_id).exists():
                        cur_genre = Genre(
                            id=genre_id, title=genre_dict[genre_id])
                        cur_genre.save()
                    else:
                        cur_genre = Genre.objects.get(id=genre_id)
                    new_movie.genres.add(cur_genre.id)

    movies = Movie.objects.all()
    serializer = MovieSerializer(movies, many=True)
    return Response(serializer.data)


@api_view(["GET", "POST"])
def recommend_movies(request, user_pk):
    movies = Movie.objects.none()

    if request.method == 'POST':
        selected_genres = request.data['genres']
        for selected in selected_genres:
            prefer = Prefer.objects.filter(user_id=user_pk, genre_id=selected)
            if prefer.exists():
                prefer[0].rank += 1
            else:
                prefer = Prefer(user_id=user_pk, genre_id=selected, rank=1)
                prefer.save()

    user_prefer = [x.genre_id for x in Prefer.objects.filter(user_id=user_pk)]
    # case 1: most prefer genre
    if len(user_prefer) == 1:
        temp_movies = Movie.genres.filter(genre_id=user_prefer[0])
        movies |= temp_movies
        if len(movies) >= 10:
            pks = random.sample(range(1, len(movies)), 10)
            movies = movies.filter(id__in=pks)
            serializer = MovieSerializer(movies,  many=True)
            return Response(serializer.data)

    # case 2: contain some genres
    if user_prefer:
        for i in range(len(user_prefer), 0, -1):
            for com in coms(user_prefer, i):
                temp_movies = Movie.objects.all()
                for cur_genre in com:
                    temp_movies = temp_movies.filter(genres=cur_genre)
                movies |= temp_movies
                if len(movies) >= 10:
                    pks = random.sample(range(1, len(movies)), 10)
                    temp_movies = movies.filter(id__in=pks)
                    serializer = MovieSerializer(temp_movies,  many=True)
                    return Response(serializer.data)

    pks = random.sample(range(1, 1000), 10 - len(movies))
    temp_movies = Movie.objects.filter(id__in=pks)
    movies |= temp_movies
    serializer = MovieSerializer(movies, many=True)
    return Response(serializer.data)


def search_movies(request, target):
    target_words = target.strip().split()
    movie = Movie.objects.none()
    for i in range(len(target_words), 0, -1):
        for com in coms(target_words, i):
            movie |= Movie.objects.filter(title__contains=list(com))
    serializer = MovieSerializer(movie, many=True)
    return Response(serializer.data)