from rest_framework import serializers
from dealers.models import MotorcycleDealer
from motorcycles.serializers import MotorcycleSerializer
from dealers.serializers import DealerSerializer


class MotorcycleDealerSerializer(serializers.ModelSerializer):
    dealer = DealerSerializer()
    motorcycle = MotorcycleSerializer()

    class Meta:
        model = MotorcycleDealer
        fields = ['id', 'dealer', 'motorcycle', 'stock']
