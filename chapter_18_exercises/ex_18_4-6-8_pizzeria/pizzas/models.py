from django.db import models

from django.db import models

class Pizza(models.Model):
    """A series of pizzas available."""
    name = models.CharField(max_length=25)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return a string representation of the model."""
        return self.name

class Topping(models.Model):
    """Ingredients to add to the Pizza."""
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    name = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return a string representation of the model."""
        return self.name
