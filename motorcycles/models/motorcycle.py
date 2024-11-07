from django.db import models
from motorcycles.models.brand import Brand
from motorcycles.models.category import Category
from motorcycles.models.engine import Engine


class Motorcycle(models.Model):
    model = models.CharField(max_length=100, unique=True)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    engine = models.ForeignKey(Engine, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    year_of_manufacture = models.PositiveIntegerField()
    color = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.model
