from rest_framework.response import Response
from rest_framework.decorators import api_view

from .fixtures.MakeMovieData import URLMaker
from .models import Movie, Prefer
from .serializers import MovieSerializer

import requests
import random
from itertools import combinations as coms
from functools import reduce


@api_view(['GET'])
def movie_list(request):
    movies = Movie.objects.all()
    serializer = MovieSerializer(movies, many=True)
    return Response(serializer.data)


@api_view(["GET", "POST"])
def recommend_movies(request, user_pk):
    genre_url = URLMaker()
    genre_json = requests.get(genre_url.getGenres()).json()
    genre_list = [x['name'] for x in genre_json['genres']]
    genre_list.sort()
    movies = Movie.objects.none()
    rank = {}
    prefer = Prefer.objects.get(pk=user_pk)

    if not Prefer.objects.get(pk=user_pk).exists():
        Prefer.objects.create(user=user_pk, prefer_movie_genre=[0] * 19)

    if request.method == 'POST':
        selected_movie_genres = request.data['genres']
        for genre in selected_movie_genres:
            prefer[genre_list.index(genre)] += 1
        prefer.save()

    for i in range(19):
        if prefer[i]:
            if prefer[i] in rank:
                rank[prefer[i]].append(i)
            else:
                rank[prefer[i]] = [i]

    # case 1: most prefer genre
    if len(rank[max(rank.keys())]) == 1:
        movies += Movie.objects.filter(genres__contains=genre_list[rank[max(rank.keys())][0]])
        if len(movies) >= 10:
            serializer = MovieSerializer(random.sample(movies, 10), many=True)
            return Response(serializer.data)

    # case 2: contain some genres
    prefer_genre = reduce(lambda x, m: x + m, rank.values(), [])
    for i in range(len(prefer_genre), -1, -1):
        for com in coms(prefer_genre, i):
            movies += Movie.objects.filter(genres__contains=[genre_list[x] for x in com])
            if len(movies) >= 10:
                serializer = MovieSerializer(random.sample(movies, 10), many=True)
                return Response(serializer.data)
    pks = random.sample(range(1, 1001), 10 - len(movies))
    movies = Movie.objects.filter(pk__in=pks)
    serializer = MovieSerializer(movies, many=True)
    return Response(serializer.data)


def search_movies(request):
    pass
