from django.db import models


class Dealer(models.Model):
    name = models.CharField(max_length=100, unique=True)
    location = models.CharField(max_length=100, blank=True, null=True)
    contact_info = models.CharField(max_length=255)

    def __str__(self):
        return self.name
