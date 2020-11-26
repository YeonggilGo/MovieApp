from django.db import models
from django.conf import settings


class Genre(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=20)


class Movie(models.Model):
    title = models.CharField(max_length=100)
    origin_title = models.CharField(max_length=100)
    overview = models.CharField(max_length=1000, null=True, blank=True)
    genres = models.ManyToManyField(Genre, related_name='genre_movie')
    poster_path = models.CharField(max_length=500, null=True, blank=True)
    backdrop_path = models.CharField(max_length=500, null=True, blank=True)
    popularity = models.FloatField()
    vote_count = models.IntegerField()
    video = models.BooleanField()
    adult = models.BooleanField()
    origin_language = models.CharField(max_length=10)
    vote_average = models.FloatField()
    release_date = models.CharField(max_length=20, null=True, blank=True)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_movies')


class Review(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    username = models.CharField(max_length=100)
    content = models.TextField()
    score = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
