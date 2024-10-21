from django.db import models
from motorcycles.models import Motorcycle

class Customer(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)  # Унікальний email
    phone = models.CharField(max_length=20, blank=True, null=True)  # Номер телефону може бути порожнім

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class Purchase(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)  # Зв'язок з клієнтом
    motorcycle = models.ForeignKey(Motorcycle, on_delete=models.CASCADE)  # Зв'язок з мотоциклом
    purchase_date = models.DateField()  # Дата покупки
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Ціна з двома десятковими місцями

    def __str__(self):
        return f'{self.customer} bought {self.motorcycle.model}'

class Review(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)  # Зв'язок з клієнтом
    motorcycle = models.ForeignKey(Motorcycle, on_delete=models.CASCADE)  # Зв'язок з мотоциклом
    rating = models.PositiveIntegerField(choices=[(i, str(i)) for i in range(1, 6)])  # Оцінка від 1 до 5
    comment = models.TextField(blank=True, null=True)  # Відгук може бути порожнім
    review_date = models.DateField(auto_now_add=True)  # Дата написання відгуку (автоматично додається)

    class Meta:
        unique_together = ('customer', 'motorcycle')  # Клієнт може залишити тільки один відгук на мотоцикл

    def __str__(self):
        return f'Review by {self.customer} for {self.motorcycle.model}'
