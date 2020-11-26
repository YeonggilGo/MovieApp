from django.urls import path
from . import views

app_name = 'community'
urlpatterns = [
    path('', views.article_list_create),
    path('<article_pk>/detail', views.article_detail),
    path('<article_pk>/', views.article_update_delete),
    path('<article_pk>/comments', views.comment_list_create),
    path('comments/<int:comment_pk>/delete', views.comments_delete),
]
