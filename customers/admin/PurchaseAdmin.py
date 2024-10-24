from django.contrib import admin
from motorcycle_project.customers.models import Purchase


@admin.register(Purchase)
class PurchaseAdmin(admin.ModelAdmin):
    list_display = ('customer', 'motorcycle', 'purchase_date', 'price')
    list_filter = ('purchase_date',)
    search_fields = ('customer__first_name', 'customer__last_name', 'motorcycle__model')
