from django.contrib import messages
from django.core import paginator
from django.shortcuts import get_object_or_404, redirect, render

from . import forms, models


def post_create(request):
    if request.method == 'POST':
        form = forms.PostForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully Created')
            return redirect(form.instance.get_absolute_url())
        else:
            messages.error(
                request,
                'It was not possible to create the post, '
                'please check the fields'
            )
    else:
        form = forms.PostForm()
    return render(request, 'posts/form.html', {'form': form})


def post_detail(request, pk):
    post = get_object_or_404(models.Post, pk=pk)
    return render(request, 'posts/detail.html', {'post': post})


def post_list(request):
    posts_list = models.Post.objects.all()
    pages = paginator.Paginator(posts_list, 5)
    page = request.GET.get('page')

    try:
        posts = pages.page(page)
    except paginator.PageNotAnInteger:
        posts = pages.page(1)
    except paginator.EmptyPage:
        posts = pages.page(pages.num_pages)

    return render(request, 'posts/index.html', {'posts': posts})


def post_edit(request, pk):
    post = get_object_or_404(models.Post, pk=pk)
    if request.method == 'POST':
        form = forms.PostForm(request.POST, instance=post)

        if form.is_valid():
            form.save()
            messages.success(request, 'The post has been saved')
            return redirect(form.instance.get_absolute_url())
        else:
            messages.error(
                request,
                'It was not possible to update the post, '
                'please check the fields'
            )
    else:
        form = forms.PostForm(instance=post)
    return render(request, 'posts/form.html', {'form': form})


def post_delete(request, pk):
    post = get_object_or_404(models.Post, pk=pk)
    post.delete()
    messages.success(request, 'The post has been deleted')
    return redirect('posts:index')
