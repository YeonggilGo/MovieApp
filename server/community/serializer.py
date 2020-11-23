from rest_framework import serializers
from .models import Article, Comment


class ArticleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Article
        fields = ('id', 'title', 'content', 'like_users')


class CommentSeializer(serializers.ModelSerializer):

    class Meta:
        motel = Comment
        fields = ('content', 'article')