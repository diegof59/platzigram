"""Posts app URL Configuration"""

from django.urls import path

from . import views

urlpatterns = [
    path('', views.list_posts, name='feed'),
    path('posts/create/', views.create_post, name='create'),
]