from django.db import models
from customers.models.customer import Customer
from motorcycles.models.motorcycle import Motorcycle


class Purchase(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    motorcycle = models.ForeignKey(Motorcycle, on_delete=models.CASCADE)
    purchase_date = models.DateField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'{self.customer} bought {self.motorcycle.model}'
