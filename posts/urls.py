"""Posts app URL Configuration"""

from django.urls import path

from . import views

urlpatterns = [
    path('', views.PostsFeedView.as_view(), name='feed'),
    path('posts/create/', views.create_post, name='create'),
    path('posts/<int:pk>/', views.PostDetailView.as_view(), name='details'),
]