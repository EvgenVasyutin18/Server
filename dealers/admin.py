from django.contrib import admin
from .models import Dealer, MotorcycleDealer

@admin.register(Dealer)
class DealerAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'contact_info')
    search_fields = ('name', 'location')

@admin.register(MotorcycleDealer)
class MotorcycleDealerAdmin(admin.ModelAdmin):
    list_display = ('motorcycle', 'dealer', 'stock')
    list_filter = ('dealer', 'motorcycle')
    search_fields = ('dealer__name', 'motorcycle__model')
