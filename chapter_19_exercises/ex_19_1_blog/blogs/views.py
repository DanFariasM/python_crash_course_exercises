from django.shortcuts import render, redirect

from .models import BlogPost
from .forms import NewBlogPostForm

def index(request):
    """The main page for the Blog. Includes posts and dates."""
    posts = BlogPost.objects.order_by("-date_added")
    context = {"posts": posts}
    return render(request, "blogs/index.html", context)

def new_post(request):
    """Add a new post."""
    if request.method != "POST":
        # No data submitted. Create a blank form.
        form = NewBlogPostForm()
    else:
        # POST data is submitted. Process data.
        form = NewBlogPostForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("blogs:index")

    # Display a blank or invalid form.
    context = {"form": form}
    return render(request, "blogs/new_post.html", context)