from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import DjangoModelPermissions
from customers.models import Review
from customers.serializers import ReviewSerializer



class ReviewViewSet(ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [DjangoModelPermissions, ]