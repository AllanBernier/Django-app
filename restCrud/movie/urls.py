from django.urls import path
from .views import MovieListCreateView, MovieDetailView,AllMoviesListView,MovieDeleteView,MovieUpdateView

urlpatterns = [
    path('movies/', MovieListCreateView.as_view(), name='movie-list-create'), # localhost:8000/api/movies/ body { name : "movie name", director : "director name", completed : true}
    path('movies/<int:pk>/', MovieDetailView.as_view(), name='movie-detail'), # localhost:8000/api/movies/1/ 
    path('movies/all/', AllMoviesListView.as_view(), name='all-movies-list'), # localhost:8000/api/movies/all/ 
    path('movies/delete/<int:pk>/', MovieDeleteView.as_view(), name='movie-delete'), # localhost:8000/api/movies/delete/1/
    path('movies/update/<int:pk>/', MovieUpdateView.as_view(), name='movie-update'), # localhost:8000/api/movies/update/1/ body { name : "movie name", director : "director name", completed : true}
]