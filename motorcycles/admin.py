from django.contrib import admin
from .models import Brand, Engine, Category, Motorcycle

@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('name', 'country')  # Відображення цих полів в таблиці

@admin.register(Engine)
class EngineAdmin(admin.ModelAdmin):
    list_display = ('capacity', 'power', 'engine_type', 'fuel_type')  # Відображення ключових полів

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)  # Відображення назви категорії

@admin.register(Motorcycle)
class MotorcycleAdmin(admin.ModelAdmin):
    list_display = ('model', 'brand', 'engine', 'category', 'price', 'year_of_manufacture', 'color')
    list_filter = ('brand', 'category', 'year_of_manufacture')  # Фільтри в адмін-панелі
    search_fields = ('model', 'brand__name')  # Пошук за моделлю та брендом
