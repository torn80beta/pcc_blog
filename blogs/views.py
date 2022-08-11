from django.shortcuts import render

# Create your views here.


def index(request):
    """Application home page"""

    return render(request, 'blogs/index.html')
