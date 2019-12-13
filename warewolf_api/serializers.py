from rest_framework import serializers
from quartet_epcis.models import entries
from django.utils.translation import gettext as _
from warewolf_api import models


class ItemDetail:
    def __init__(self, item: entries.Entry):
        self.is_parent = str(item.is_parent)
        self.EPC = item.identifier,
        self.parent_EPC = item.parent_identifier,
        self.top_EPC = item.top_identifier,
        self.last_event = item.last_event_time
        self.last_event_id = item.last_event_id
        self.last_aggregation_event = item.last_aggregation_event_time
        self.disposition = item.last_disposition
        self.is_decomissioned = str(item.decommissioned)


class EntrySerializer(serializers.ModelSerializer):
    parent_id = serializers.SlugRelatedField(
        read_only=True,
        many=False,
        slug_field='identifier',
        label='Parent EPC'
    )
    top_id = serializers.SlugRelatedField(
        read_only=True,
        many=False,
        slug_field='identifier',
        label='Top EPC'
    )
    lot_number = serializers.SerializerMethodField()
    expiration_date = serializers.SerializerMethodField()

    def get_lot_number(self, entry):
        return entry.ilmd.get('lotNumber')

    def get_expiration_date(self, entry):
        return entry.ilmd.get('itemExpirationDate')

    class Meta:
        model = entries.Entry
        fields = '__all__'


class TransactionSerializer(serializers.ModelSerializer):
    '''
    Default serializer for the Transaction model.
    '''

    class Meta:
        model = models.Transaction
        exclude = ['record_time',
                   'event_time',
                   'event_timezone_offset',
                   ]
