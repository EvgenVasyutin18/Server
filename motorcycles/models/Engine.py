from django.db import models


class Engine(models.Model):
    capacity = models.PositiveIntegerField()
    power = models.PositiveIntegerField()
    engine_type = models.CharField(max_length=100)
    fuel_type = models.CharField(max_length=50, choices=[('Petrol', 'Petrol'), ('Electric', 'Electric')])

    def __str__(self):
        return f'{self.capacity}cc {self.engine_type}'
