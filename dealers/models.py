from django.db import models
from motorcycles.models import Motorcycle

class Dealer(models.Model):
    name = models.CharField(max_length=100, unique=True)  # Унікальна назва дилера
    location = models.CharField(max_length=100, blank=True, null=True)  # Місцезнаходження може бути порожнім
    contact_info = models.CharField(max_length=255)  # Контактна інформація (обов'язкове поле)

    def __str__(self):
        return self.name

class MotorcycleDealer(models.Model):
    motorcycle = models.ForeignKey(Motorcycle, on_delete=models.CASCADE)  # Зв'язок з мотоциклом
    dealer = models.ForeignKey(Dealer, on_delete=models.CASCADE)  # Зв'язок з дилером
    stock = models.PositiveIntegerField()  # Кількість в наявності (позитивне число)

    class Meta:
        unique_together = ('motorcycle', 'dealer')  # Унікальність пари мотоцикл-дилер

    def __str__(self):
        return f'{self.dealer.name} - {self.motorcycle.model}'
