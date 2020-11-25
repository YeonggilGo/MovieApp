from rest_framework import serializers
from .models import Article, Comment


class ArticleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Article
        fields = ('id', 'title', 'content', 'user', 'username', 'created_at', 'updated_at')


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        motel = Comment
        fields = ('content', 'article', 'created_at', 'updated_at')