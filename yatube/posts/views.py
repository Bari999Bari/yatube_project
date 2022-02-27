from django.shortcuts import render
from django.http import HttpResponse


# Main page
def index(request):
    template = 'posts/index.html'
    context = {
        'text': 'Это главная страница проекта Yatube'
    }
    return render(request, template, context)


# Posts sorted by group
def group_posts(request):
    template = 'posts/group_list.html'
    context = {
        'text': 'Здесь будет информация о группах проекта Yatube'
    }
    return render(request, template, context)
