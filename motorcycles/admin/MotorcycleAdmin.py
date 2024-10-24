from django.contrib import admin
from motorcycle_project.motorcycles.models import Motorcycle


@admin.register(Motorcycle)
class MotorcycleAdmin(admin.ModelAdmin):
    list_display = ('model', 'brand', 'engine', 'category', 'price', 'year_of_manufacture', 'color')
    list_filter = ('brand', 'category', 'year_of_manufacture')
    search_fields = ('model', 'brand__name')