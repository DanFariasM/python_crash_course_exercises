from django.shortcuts import render

def index(request):
    """The main page for the Blog."""
    return render(request, "blogs/index.html")