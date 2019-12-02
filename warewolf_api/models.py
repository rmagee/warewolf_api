# -*- coding: utf-8 -*-
import datetime
from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _
from model_utils import fields

from EPCPyYes.core.v1_2 import CBV
from quartet_output.models import EndPoint, AuthenticationInfo
from quartet_epcis.models.abstractmodels import EPCISBusinessEvent
from quartet_masterdata.models import Location, Company

EVENT_TYPE_CHOICES = (
    ('OBJECT', 'OBJECT'),
    ('AGGREGATION', 'AGGREGATION'),
    ('TRANSACTION', 'TRANSACTION')
)

ILMD_CHOICES = [(key.value, key.value) for key in CBV.LotLevelAttributeName] + \
               [(key.value, key.value) for key in
                CBV.TradeItemLevelAttributeName] + \
               [(key.value, key.value) for key in CBV.ItemLevelAttributeName]


class Transaction(EPCISBusinessEvent):
    icon = models.CharField(
        max_length=20,
        verbose_name=_("Icon"),
        help_text=_("The name of the Material-UI icon to display."),
        null=True,
        blank=False,
        default='Check'
    )
    event_time = models.DateTimeField(
        default=datetime.datetime.utcnow(),
        verbose_name=_("Created Date"),
        help_text=_("The date this transaction was initially created."),
        null=False,
        blank=False,
    )
    event_type = models.CharField(
        max_length=20,
        verbose_name=_("Event Type"),
        help_text=_("The type of EPCIS event to create."),
        null=False,
        blank=False,
        default='OBJECT'
    )
    name = models.CharField(
        max_length=200,
        verbose_name=_("Name"),
        help_text=_("The user-friendly name of this transaction."),
        null=False
    )
    description = models.CharField(
        max_length=500,
        verbose_name=_("Brief Description"),
        help_text=_("A brief description of this transaction"),
        null=True,
        blank=True
    )
    default_ship_to = models.ForeignKey(
        Location,
        verbose_name=_("Ship To"),
        related_name='default_ship_to',
        help_text=_("The default location that this transaction will "
                    "use as a ship-to-location."),
        on_delete=models.CASCADE,
        null=True, blank=True
    )
    default_ship_from = models.ForeignKey(
        Location,
        verbose_name=_("Ship From"),
        related_name='default_ship_from',
        help_text=_("The default ship from location."),
        on_delete=models.CASCADE,
        null=True, blank=True
    )
    default_possessing_party = models.ForeignKey(
        Company,
        verbose_name=_("Possessing Party"),
        related_name='default_possessing_party',
        help_text=_("The default possessing party if any."),
        on_delete=models.CASCADE,
        null=True, blank=True
    )
    default_owning_party = models.ForeignKey(
        Company,
        related_name='default_owning_party',
        verbose_name=_("Owning Party"),
        help_text=_("The default owning party if any."),
        on_delete=models.CASCADE,
        null=True, blank=True
    )
    users = models.ManyToManyField(get_user_model(),
                                   verbose_name=_("Users"),
                                   help_text=_("The users with rights to this"
                                               " transaction."))
    auto_disaggregate = models.BooleanField(
        verbose_name=_("Auto Disaggregate"),
        help_text=_("Whether or not this transaction should automagically "
                    "disaggregate items that are being packed (when "
                    "applicable)."),
        null=False,
        blank=False,
        default=False
    )
    auto_decommission_parent = models.BooleanField(
        verbose_name=_("Auto Decommission Parent"),
        help_text=_("When picking an item from a parent, should the parent "
                    "be automagically decommissioned and the rest of the "
                    "children freed up."),
        null=False,
        blank=False,
        default=False
    )
    scan_ilmd = models.BooleanField(
        verbose_name=_("Scan ILMD value"),
        help_text=_("If true, users will not scan in serialized information "
                    "but rather a lot/master data value. For example, ship "
                    "by lot number."),
        null=False,
        blank=False,
        default=False
    )
    ilmd_field = models.CharField(
        max_length=300,
        verbose_name=_("ILMD Field"),
        help_text=_("If scan by ILMD field is true, this will be the lookup "
                    "field for serialized data to include in the message."),
        null=False,
        blank=False,
        default=True,
        choices=ILMD_CHOICES
    )
    authentication_info = models.ForeignKey(
        'quartet_output.AuthenticationInfo',
        null=True, blank=True,
        on_delete=models.SET_NULL,
        verbose_name=_("Authentication Info"),
        help_text=_("The Authentication Info to use when sending transaction "
                    "data.")
    )
    end_point = models.ForeignKey(
        'quartet_output.EndPoint',
        null=True,
        blank=True,
        on_delete=models.PROTECT,
        verbose_name=_("End Point"),
        help_text=_("A prtocol-specific endpoint defining where any output"
                    " data will be sent."),
    )


class BarcodeCache(models.Model):
    """
    To prevent the repeated lookup of barcode values and their conversion
    to URNs, etc.  Basically a lookup cache.
    """
    barcode = models.CharField(
        max_length=200,
        verbose_name=_("Barcode"),
        help_text=_("The barcode that was queried."),
        null=False,
        blank=False
    )
    created = fields.AutoCreatedField(
        verbose_name=_("Created"),
        help_text=_("Create date."),
        null=False
    )
