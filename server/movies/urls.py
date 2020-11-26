from django.urls import path
from . import views

urlpatterns = [
    path('', views.movie_list),
    path('popular', views.popular_movies),
    path('genre/<int:genre_id>', views.genre_movies),
    path('detail/<int:movie_pk>', views.movie_detail),
    path('recommend', views.recommend_movies),
    path('search', views.search_movies),
    path('<movie_pk>/like', views.movie_like),

    path('<movie_pk>/review', views.review_list_create),
    path('<movie_pk>/review/<int:review_pk>/', views.review_update_delete),
]