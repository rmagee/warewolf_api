from rest_framework import routers
from warewolf_api import viewsets

router = routers.DefaultRouter()

router.register(
    r'transactions',
    viewsets.TransactionViewSet,
    basename='transactions'
)

