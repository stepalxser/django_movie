from django.urls import path

from . import views

urlpatterns = [
    path('', views.MovieView.as_view()),
    path('<slug:slug>/', views.MovieDetailVIew.as_view(), name='movie_detail'),
    path('<int:pk>', views.AddReview.as_view(), name='add_review'),
]