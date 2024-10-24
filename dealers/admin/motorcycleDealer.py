from django.contrib import admin
from motorcycle_project.dealers.models import MotorcycleDealer


@admin.register(MotorcycleDealer)
class MotorcycleDealerAdmin(admin.ModelAdmin):
    pass
