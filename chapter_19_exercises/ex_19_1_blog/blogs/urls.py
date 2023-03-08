"""Defines URL patterns for the Blogs app."""

from django.urls import path

from . import views

app_name = "blogs"
urlpatterns = [
    # Main page
    path("", views.index, name="index"),
    # Page for adding a new post
    path("new_post/", views.new_post, name="new_post"),
]