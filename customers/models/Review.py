from django.db import models

from motorcycle_project.customers.models.Customer import Customer
from motorcycle_project.customers.models import Motorcycle


class Review(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    motorcycle = models.ForeignKey(Motorcycle, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField(choices=[(i, str(i)) for i in range(1, 6)])
    comment = models.TextField(blank=True, null=True)
    review_date = models.DateField(auto_now_add=True)

    class Meta:
        unique_together = ('customer', 'motorcycle')

    def __str__(self):
        return f'Review by {self.customer} for {self.motorcycle.model}'
