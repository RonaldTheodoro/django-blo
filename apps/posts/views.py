from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render

from . import models


def index(request):
    return render(request, 'index.html', {})

def post_create(request):
    return render(request, 'posts/create.html', {})


def post_detail(request, pk):
    post = get_object_or_404(models.Post, pk=pk)
    return render(request, 'posts/detail.html', {'post': post})


def post_list(request):
    posts = models.Post.objects.all()
    return render(request, 'posts/list.html', {'posts': posts})


def post_update(request):
    return render(request, 'posts/update.html', {})


def post_delete(request):
    return render(request, 'posts/delete.html', {})
