from rest_framework import serializers
from customers.models import Purchase
from motorcycles.serializers.motorcycle import MotorcycleSerializer
from customers.serializers.customer import CustomerSerializer


class PurchaseSerializer(serializers.ModelSerializer):
    customer = CustomerSerializer()
    motorcycle = MotorcycleSerializer()

    class Meta:
        model = Purchase
        fields = ['id', 'customer', 'motorcycle', 'purchase_date', 'price']
