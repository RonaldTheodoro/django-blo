from django.contrib import messages
from django.core import paginator
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.admin.views.decorators import staff_member_required
from . import forms, models


@staff_member_required
def post_create(request):
    if request.method == 'POST':
        form = forms.PostForm(data=request.POST, files=request.FILES)

        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            messages.success(request, 'Successfully Created')
            return redirect(post.get_absolute_url())
        else:
            messages.error(
                request,
                'It was not possible to create the post, '
                'please check the fields'
            )
    else:
        form = forms.PostForm()
    return render(request, 'posts/form.html', {'form': form})


def post_detail(request, slug):
    post = get_object_or_404(models.Post, slug=slug)
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

@staff_member_required
def post_edit(request, slug):
    post = get_object_or_404(models.Post, slug=slug)
    if request.method == 'POST':
        form = forms.PostForm(
            data=request.POST,
            files=request.FILES,
            instance=post
        )

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

@staff_member_required
def post_delete(request, slug):
    post = get_object_or_404(models.Post, slug=slug)
    post.delete()
    messages.success(request, 'The post has been deleted')
    return redirect('posts:index')
