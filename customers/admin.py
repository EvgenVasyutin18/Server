from django.contrib import admin
from .models import Customer, Purchase, Review

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'phone')
    search_fields = ('first_name', 'last_name', 'email')

@admin.register(Purchase)
class PurchaseAdmin(admin.ModelAdmin):
    list_display = ('customer', 'motorcycle', 'purchase_date', 'price')
    list_filter = ('purchase_date',)
    search_fields = ('customer__first_name', 'customer__last_name', 'motorcycle__model')

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('customer', 'motorcycle', 'rating', 'review_date')
    list_filter = ('rating', 'review_date')
    search_fields = ('customer__first_name', 'customer__last_name', 'motorcycle__model')
