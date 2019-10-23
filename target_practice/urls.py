from django.urls import path
import app.views
from django.contrib import admin

urlpatterns = [
    path("add", app.views.add, name="add"),
    path("subtract", app.views.subtract, name="subtract"),
    path("name", app.views.name, name="name"),
    path("movies", app.views.movies, name="movies"),
    path("rating", app.views.rating, name="rating")
]
