from django.db import models
from django.core.validators import MinValueValidator

class Menu(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2, validators=[
        MinValueValidator(0.01)  # Harga minimal adalah 0.01
    ])
    category = models.CharField(max_length=255)

    def __str__(self):
        return self.name
