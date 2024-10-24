from django.contrib import admin
from motorcycle_project.motorcycles.models import Brand


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('name', 'country')
