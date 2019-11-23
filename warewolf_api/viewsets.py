from rest_framework.viewsets import ModelViewSet
from warewolf_api import models, serializers


class TransactionViewSet(ModelViewSet):
    '''
    CRUD ready model view for the Transaction model.
    '''
    queryset = models.Transaction.objects.all()
    serializer_class = serializers.TransactionSerializer

