from django.shortcuts import render
from django.http import HttpResponse
from .models import Blog

# Create your views here.

def index(request):

    blogs = Blog.objects.all()[:10]

    context = {
        'Title' : 'Recent Posts',
        'Blog' : blogs
    }

    return render(request, 'blog/index.html', context)


def details(request, id):
    blog = Blog.objects.get(id=id)

    context = {
        'blog' : blog
    }

    return render(request, 'blog/details.html', context)