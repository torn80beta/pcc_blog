from django.shortcuts import render
from . models import BlogPost

# Create your views here.


def index(request):
    """Application home page"""
    posts = BlogPost.objects.order_by('-date_added')
    context = {'posts': posts}
    return render(request, 'blogs/index.html', context)
