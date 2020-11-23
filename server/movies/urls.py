from django.urls import path
from . import views

urlpatterns = [
    path('<int:page>', views.movie_list),
    path('popular', views.popular_movies),
    path('<str:genre>', views.genre_movies),
    path('detail/<int:movie_pk>', views.movie_detail),
    path('recommend/<int:user_pk>', views.recommend_movies),
    path('search/<str:target>', views.search_movies),
]