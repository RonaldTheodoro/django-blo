from django.urls import path

from . import views


app_name = 'posts'

urlpatterns = [
    path('', views.post_list, name='index'),
    path('new', views.post_create, name='create'),
    path('<int:pk>', views.post_detail, name='detail'),
    path('edit', views.post_update, name='update'),
    path('delete', views.post_delete, name='delete'),
]
