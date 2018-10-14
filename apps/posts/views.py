from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect

from . import forms, models


def post_create(request):
    if request.method == 'POST':
        form = forms.PostForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect(form.instance.get_absolute_url())
    else:
        form = forms.PostForm()
    return render(request, 'posts/form.html', {'form': form})


def post_detail(request, pk):
    post = get_object_or_404(models.Post, pk=pk)
    return render(request, 'posts/detail.html', {'post': post})


def post_list(request):
    posts = models.Post.objects.all()
    return render(request, 'posts/index.html', {'posts': posts})


def post_edit(request, pk):
    post = get_object_or_404(models.Post, pk=pk)
    if request.method == 'POST':
        form = forms.PostForm(request.POST, instance=post)

        if form.is_valid():
            form.save()
            return redirect(form.instance.get_absolute_url())
    else:
        form = forms.PostForm(instance=post)
    return render(request, 'posts/form.html', {'form': form})


def post_delete(request):
    return render(request, 'posts/delete.html', {})
