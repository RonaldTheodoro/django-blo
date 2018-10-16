from django.urls import path

from . import views


app_name = 'posts'

urlpatterns = [
    path('', views.post_list, name='index'),
    path('new', views.post_create, name='create'),
    path('<slug:slug>', views.post_detail, name='detail'),
    path('<slug:slug>/edit', views.post_edit, name='edit'),
    path('<slug:slug>/delete', views.post_delete, name='delete'),
]
