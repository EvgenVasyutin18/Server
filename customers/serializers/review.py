from rest_framework import serializers
from customers.models import Review
from motorcycles.serializers.motorcycle import MotorcycleSerializer
from customers.serializers.customer import CustomerSerializer


class ReviewSerializer(serializers.ModelSerializer):
    customer = CustomerSerializer()
    motorcycle = MotorcycleSerializer()

    class Meta:
        model = Review
        fields = ['id', 'customer', 'motorcycle', 'rating', 'comment', 'review_date']
