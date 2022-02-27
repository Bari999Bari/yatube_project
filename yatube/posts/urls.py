from django.urls import path

from . import views

app_name = 'posts'

urlpatterns = [
    path('', views.index, name='main'),
    path('group_list/', views.group_posts, name='group_posts')
]
