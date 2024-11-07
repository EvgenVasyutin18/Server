from rest_framework import serializers
from motorcycles.models import Motorcycle
from motorcycles.serializers.brand import BrandSerializer
from motorcycles.serializers.engine import EngineSerializer
from motorcycles.serializers.category import CategorySerializer


class MotorcycleSerializer(serializers.ModelSerializer):
    brand = BrandSerializer()
    engine = EngineSerializer()
    category = CategorySerializer()

    class Meta:
        model = Motorcycle
        fields = [
            'id', 'model', 'brand', 'engine', 'category',
            'price', 'year_of_manufacture', 'color', 'description'
        ]
