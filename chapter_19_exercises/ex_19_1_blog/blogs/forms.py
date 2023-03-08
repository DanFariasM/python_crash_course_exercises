from django import forms

from .models import BlogPost

class NewBlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ["title", "text"]
        labels = {"title": "Title:", "text": "Post:"}
        widgets = {"text": forms.Textarea(attrs={"cols": 40,})}
