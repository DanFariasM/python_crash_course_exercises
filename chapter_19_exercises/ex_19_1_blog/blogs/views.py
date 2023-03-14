from django.shortcuts import render, redirect

from .models import BlogPost
from .forms import BlogPostForm

def index(request):
    """The main page for the Blog. Includes posts and dates."""
    posts = BlogPost.objects.order_by("-date_added")
    context = {"posts": posts}
    return render(request, "blogs/index.html", context)

def new_post(request):
    """Add a new post."""
    if request.method != "POST":
        # No data submitted. Create a blank form.
        form = BlogPostForm()
    else:
        # POST data is submitted. Process data.
        form = BlogPostForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("blogs:index")

    # Display a blank or invalid form.
    context = {"form": form}
    return render(request, "blogs/new_post.html", context)

def edit_post(request, post_id):
    """Edit an existing post."""
    post = BlogPost.objects.get(id=post_id)

    if request.method != "POST":
        # Initial request; pre-fill the form with the current post.
        form = BlogPostForm(instance=post)
    else:
        # POST data submitted; process data.
        form = BlogPostForm(instance=post, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("blogs:index")

    context = {"post": post, "form": form}
    return render(request, "blogs/edit_post.html", context)