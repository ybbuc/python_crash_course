from django.db import models

class Pizza(models.Model):
    """A simple model for a pizza."""
    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name

class Topping(models.Model):
    """A simple model for a topping to add to a pizza."""
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name
