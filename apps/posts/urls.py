from django.urls import path

from . import views


app_name = 'posts'

urlpatterns = [
    path('create', views.post_create, name='create'),
    path('detail', views.post_detail, name='detail'),
    path('list', views.post_list, name='list'),
    path('update', views.post_update, name='update'),
    path('delete', views.post_delete, name='delete'),
]
