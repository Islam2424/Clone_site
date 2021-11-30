from django.http import HttpResponse
from django.shortcuts import render

posts = [
    {
        'author': 'Corey MS',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'August 15 2015'
    },
    {
        'author': 'Aleksey Mikhailov',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'September 22 2012'
    }
]


def home(request):
    context = {
        'posts': posts,
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
