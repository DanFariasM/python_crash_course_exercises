from django.shortcuts import render

from .models import BlogPost

def index(request):
    """The main page for the Blog. Includes posts and dates."""
    posts = BlogPost.objects.all()
    context = {"posts": posts}
    return render(request, "blogs/index.html", context)