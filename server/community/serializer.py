from rest_framework import serializers
from .models import Article, Comment


class ArticleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Article
        fields = ('id', 'title', 'content', 'username', 'created_at', 'updated_at')


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        motel = Comment
        fields = ('username', 'content', 'created_at', 'updated_at')