from django.db import models
from motorcycle_project.dealers.models import Motorcycle, Dealer


class MotorcycleDealer(models.Model):
    motorcycle = models.ForeignKey(Motorcycle, on_delete=models.CASCADE)
    dealer = models.ForeignKey(Dealer, on_delete=models.CASCADE)
    stock = models.PositiveIntegerField()

    class Meta:
        unique_together = ('motorcycle', 'dealer')

    def __str__(self):
        return f'{self.dealer.name} - {self.motorcycle.model}'


