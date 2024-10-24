from django.contrib import admin
from motorcycle_project.motorcycles.models import Engine


@admin.register(Engine)
class EngineAdmin(admin.ModelAdmin):
    list_display = ('capacity', 'power', 'engine_type', 'fuel_type')
