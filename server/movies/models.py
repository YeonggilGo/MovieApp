from django.db import models
from django.conf import settings


class Genre(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=20)


class Movie(models.Model):
    title = models.CharField(max_length=100)
    origin_title = models.CharField(max_length=100)
    overview = models.CharField(max_length=1000)
    genres = models.ManyToManyField(Genre, related_name='genre_movie')
    poster_path = models.CharField(max_length=500)
    backdrop_path = models.CharField(max_length=500, null=True, blank=True)
    popularity = models.FloatField()
    vote_count = models.IntegerField()
    video = models.BooleanField()
    adult = models.BooleanField()
    origin_language = models.CharField(max_length=10)
    vote_average = models.FloatField()
    release_date = models.CharField(max_length=20)



class Prefer(models.Model):
    user_id = models.IntegerField()
    genre_id = models.IntegerField()
    rank = models.IntegerField()


"popularity": 1307.787,
"vote_count": 209,
 "video": false,
  "id": 671039,
  "adult": false,
   "original_language": "fr",
    "vote_average": 6,
    "release_date": "2020-10-30"
