from django.shortcuts import render
from django.http import HttpResponse


# Main page
def index(request):
    return HttpResponse(f'Главная страница')


# Posts sorted by group
def group_posts(request, my_slug):
    return HttpResponse(f'Посты отфильтрованные по группам {my_slug}')
