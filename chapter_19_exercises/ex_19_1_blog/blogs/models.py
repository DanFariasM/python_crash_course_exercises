from django.db import models

class BlogPost(models.Model):
    """A post the user wants to share in the blog."""
    title = models.CharField(max_length=50)
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return a string representation of the model."""
        return self.text