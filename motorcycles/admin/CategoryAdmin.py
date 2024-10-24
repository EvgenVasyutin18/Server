from django.contrib import admin
from motorcycle_project.motorcycles.models import Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
