from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import DjangoModelPermissions
from customers.models import Purchase
from customers.serializers import PurchaseSerializer



class PurchaseViewSet(ModelViewSet):
    queryset = Purchase.objects.all()
    serializer_class = PurchaseSerializer
    permission_classes = [DjangoModelPermissions, ]