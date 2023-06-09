from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import Http404

from .models import BlogPost
from .forms import BlogPostForm

def index(request):
    """The main page for the Blog. Includes posts and dates."""
    posts = BlogPost.objects.order_by("-date_added")
    context = {"posts": posts}
    return render(request, "blogs/index.html", context)

@login_required
def new_post(request):
    """Add a new post."""
    if request.method != "POST":
        # No data submitted. Create a blank form.
        form = BlogPostForm()
    else:
        # POST data is submitted. Process data.
        form = BlogPostForm(data=request.POST)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.owner = request.user
            new_post.save()
            return redirect("blogs:index")

    # Display a blank or invalid form.
    context = {"form": form}
    return render(request, "blogs/new_post.html", context)

@login_required
def edit_post(request, post_id):
    """Edit an existing post."""
    post = BlogPost.objects.get(id=post_id)

    if post.owner != request.user:
        raise Http404

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