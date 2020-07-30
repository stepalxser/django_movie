from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView

from .models import Movie


class MovieView(ListView):
    model = Movie
    queryset = Movie.objects.filter(draft=False)


class MovieDetailVIew(DetailView):
    model = Movie
    slug_field = 'url'

