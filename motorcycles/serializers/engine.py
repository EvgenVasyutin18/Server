from rest_framework import serializers
from motorcycles.models import Engine


class EngineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Engine
        fields = ['id', 'capacity', 'power', 'engine_type', 'fuel_type']
