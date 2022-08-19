from django.shortcuts import render, redirect
from .models import BlogPost
from .forms import PostForm

# Create your views here.


def index(request):
    """Application home page"""
    posts = BlogPost.objects.order_by('-date_added')
    context = {'posts': posts}
    return render(request, 'blogs/index.html', context)


def post(request, post_id):
    # Single post page
    post = BlogPost.objects.get(id=post_id)
    entries = {post.entry_set}
    text = post.text
    context = {'post': post, 'entries': entries, 'text': text}
    return render(request, 'blogs/post.html/', context)


def new_post(request):
    """New post definition"""
    if request.method != 'POST':
        # Empty form creation
        form = PostForm()
    else:
        # Data processing
        form = PostForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('blogs:index')
    # Empty or invalid form output
    context = {'form': form}
    return render(request, 'blogs/new_post.html', context)


