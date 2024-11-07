from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import DjangoModelPermissions

from customers.models import Customer
from customers.serializers import CustomerSerializer


class CustomerViewSet(ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = [DjangoModelPermissions, ]
