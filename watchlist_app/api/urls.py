from django.urls import path

from watchlist_app.api import views

urlpatterns = [
    path('list/',views.movie_list,name="movie-list"),
    path('list/<int:pk>/',views.movie_details,name="movie-details")
]


