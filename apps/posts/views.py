from django.shortcuts import render
from django.http import HttpResponse


def post_create(request):
    return HttpResponse('<h1>Hello World</h1>')


def post_detail(request):
    return HttpResponse('<h1>Hello World</h1>')


def post_list(request):
    return HttpResponse('<h1>Hello World</h1>')


def post_update(request):
    return HttpResponse('<h1>Hello World</h1>')


def post_delete(request):
    return HttpResponse('<h1>Hello World</h1>')
