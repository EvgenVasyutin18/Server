from django.contrib import admin
from motorcycle_project.customers.models import Review


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('customer', 'motorcycle', 'rating', 'review_date')
    list_filter = ('rating', 'review_date')
    search_fields = ('customer__first_name', 'customer__last_name', 'motorcycle__model')
