from django.urls import path
from . import views

app_name = 'community'
urlpatterns = [
    path('', views.article_list_create),
    path('<article_pk>/', views.article_detail),
    path('<article_pk>/comments', views.comment_create, name='comment_create'),
    path('<article_pk>/comments/<int:comment_pk>/delete', views.comments_delete, name='comments_delete'),
    path('<article_pk>/like/', views.article_like, name='like'),
]
