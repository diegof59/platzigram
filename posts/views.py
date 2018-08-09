from django.shortcuts import render
from django.http import HttpResponse


def list_posts(request):
	posts = 'En construcción'
	return HttpResponse(posts)
