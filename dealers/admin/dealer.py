from django.contrib import admin
from motorcycle_project.dealers.models import Dealer


@admin.register(Dealer)
class DealerAdmin(admin.ModelAdmin):
    pass