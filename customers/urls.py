from rest_framework.routers import DefaultRouter
from customers.views.customer import CustomerViewSet
from customers.views.purchase import PurchaseViewSet
from customers.views.review import ReviewViewSet

router = DefaultRouter()
router.register(r'customer', CustomerViewSet)
router.register(r'purchase', PurchaseViewSet)
router.register(r'review', ReviewViewSet)

urlpatterns = [] + router.urls
