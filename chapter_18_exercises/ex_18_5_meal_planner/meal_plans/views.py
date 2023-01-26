from django.shortcuts import render

def index(request):
    """The home pahe for meal plans."""
    return render(request, "meal_plans/index.html")