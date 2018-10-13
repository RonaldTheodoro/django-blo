from django.urls import path

from . import views


app_name = 'posts'

urlpatterns = [
    path('', views.index, name='index'),
    path('new', views.post_create, name='create'),
    path('<int:pk>', views.post_detail, name='detail'),
    path('list', views.post_list, name='list'),
    path('edit', views.post_update, name='update'),
    path('delete', views.post_delete, name='delete'),
]