from django.shortcuts import render
from django.http import HttpResponse


def post_create(request):
    return render(request, 'create.html', {})


def post_detail(request):
    return render(request, 'detail.html', {})


def post_list(request):
    return render(request, 'list.html', {})


def post_update(request):
    return render(request, 'update.html', {})


def post_delete(request):
    return render(request, 'delete.html', {})
