"""
URL configuration for libraryapi project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from movies.views import (
    get_all_movies,
    movie_by_id,
    search_movies,
    create_movie,
    get_summary,
    get_top_movies,
    welcome,
    get_geojson
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('movies/', get_all_movies, name='get_all_movies'),
    path('movies/<int:id>/', movie_by_id, name='get_movie_by_id'),
    path('search/', search_movies, name='search_movies'),
    path('movies/', create_movie, name='create_movie'),
    path('summary/', get_summary, name='get_summary'),
    path('top/', get_top_movies, name='get_top_movies'),
    path('', welcome, name='welcome'),
    path('geojson/', get_geojson, name='get_geojson')
]
