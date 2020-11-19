from django.urls import path
from . import views

urlpatterns = [
    path('', views.movie_list),
    path('recommend/<int:user_pk>', views.recommend_movies),
    path('search', views.search_movies),
]