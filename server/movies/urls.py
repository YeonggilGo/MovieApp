from django.urls import path
from . import views

urlpatterns = [
    path('<int:page>', views.movie_list),
    path('popular', views.popular_movies),
    path('genre/<int:genre_id>/<int:page>', views.genre_movies),
    path('detail/<int:movie_pk>', views.movie_detail),
    path('recommend/<int:user_pk>', views.recommend_movies),
    path('search', views.search_movies),
    path('<movie_pk>/like/', views.movie_like, name='like'),
]