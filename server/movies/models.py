from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.conf import settings


class Movie(models.Model):
    title = models.CharField(max_length=100)
    origin_title = models.CharField(max_length=100)
    overview = models.CharField(max_length=1000)
    genres = ArrayField(models.CharField(max_length=20))
    poster_path = models.CharField(max_length=500)
    backdrop_path = models.CharField(max_length=500, null=True, blank=True)


class Prefer(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    genre_prefer_rank = ArrayField(models.IntegerField())
