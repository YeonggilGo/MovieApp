from rest_framework import serializers
from .models import Movie


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('id', 'title', 'origin_title', 'poster_path', 'backdrop_path', 'overview', 'genres')
