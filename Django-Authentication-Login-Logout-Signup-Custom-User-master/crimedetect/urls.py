

from django.shortcuts import render
from django.urls import path
from . import views

# Create your views here.
urlpatterns = [path("search", views.search_crime_in_place, name="search")]



