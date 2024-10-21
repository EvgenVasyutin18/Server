from django.db import models

class Brand(models.Model):
    name = models.CharField(max_length=100, unique=True)  # Унікальна назва бренду
    country = models.CharField(max_length=100, blank=True, null=True)  # Країна може бути не вказана

    def __str__(self):
        return self.name

class Engine(models.Model):
    capacity = models.PositiveIntegerField()  # Об'єм двигуна (лише додатні значення)
    power = models.PositiveIntegerField()  # Потужність (лише додатні значення)
    engine_type = models.CharField(max_length=100)  # Тип двигуна
    fuel_type = models.CharField(max_length=50, choices=[('Petrol', 'Petrol'), ('Electric', 'Electric')])

    def __str__(self):
        return f'{self.capacity}cc {self.engine_type}'

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)  # Унікальна назва категорії

    def __str__(self):
        return self.name

class Motorcycle(models.Model):
    model = models.CharField(max_length=100, unique=True)  # Унікальна назва моделі мотоцикла
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    engine = models.ForeignKey(Engine, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)  # Категорія може бути невизначена
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Ціна з двома десятковими місцями
    year_of_manufacture = models.PositiveIntegerField()  # Рік випуску, тільки позитивні числа
    color = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)  # Опис може бути порожнім

    def __str__(self):
        return self.model
