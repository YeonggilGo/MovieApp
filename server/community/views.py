from django.shortcuts import get_object_or_404

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from .models import Comment, Article
from .serializer import ArticleSerializer, CommentSerializer


@api_view(['GET', 'POST'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def article_list_create(request):
    if request.method == 'POST':
        Article.objects.create(
            title=request.data['title'],
            content=request.data['content'],
            user=request.user,
            username=request.user.username,
        )
        article = Article.objects.get(title=request.data['title'])
        article.save()
        serializer = ArticleSerializer(article)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
    else:
        page = int(request.GET.get('page'))
        articles = Article.objects.all()[(page - 1) * 10:page * 10]
        cnt_articles = Article.objects.count()
        serializer = [ArticleSerializer(articles, many=True).data, {
            'cnt_articles': cnt_articles,
        }]
        return Response(serializer)


@api_view(['GET', 'PUT', ' DELETE'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def article_update_delete(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    if request.user != article.user:
        return Response({'error': 'Not available'}, status=status.HTTP_401_UNAUTHORIZED)

    if request.method == 'GET':
        serializer = ArticleSerializer(article)
        return Response(serializer.data)
    elif request.method == 'PUT':
        article.title = request.data.title
        article.content = request.data.content
        serializer = ArticleSerializer(article)
        serializer.save()
        return Response(serializer.data)
    elif request.method == 'DELETE':
        article.delete()
        return Response({'id': article_pk})


@api_view(['GET'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def article_detail(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    serializer = ArticleSerializer(data=article)
    if serializer.is_valid(raise_exception=True):
        return Response(serializer.data)


@api_view(['GET', 'POST'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def comment_list_create(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    if request.method == 'POST':
        serializer = CommentSerializer(request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user, article=article)
            return Response(serializer.data)
    else:
        comments = Comment.objects.filter(article=article)
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)


@api_view(['GET', 'PUT', 'DELETE'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def comments_delete(request, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)

    if request.user != comment.user:
        return Response({'error': 'Not available'}, status=status.HTTP_401_UNAUTHORIZED)

    if request.method == 'DELETE':
        comment.delete()
        return Response({'id': comment_pk})
    elif request.method == 'GET':
        serializer = CommentSerializer(comment)
        return Response(serializer.data)
    else:
        comment.content = request.data.content
        serializer = CommentSerializer(comment)
        serializer.save()
        return Response(serializer.data)
