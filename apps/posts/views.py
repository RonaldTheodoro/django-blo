from django.shortcuts import render
from django.http import HttpResponse

from . import models


def index(request):
    return render(request, 'index.html', {})

def post_create(request):
    return render(request, 'posts/create.html', {})


def post_detail(request):
    return render(request, 'posts/detail.html', {})


def post_list(request):
    posts = models.Post.objects.all()
    return render(request, 'posts/list.html', {'posts': posts})


def post_update(request):
    return render(request, 'posts/update.html', {})


def post_delete(request):
    return render(request, 'posts/delete.html', {})
