# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth import get_user_model
from quartet_masterdata.models import Location, Company
from django.utils.translation import gettext_lazy as _
from model_utils import fields, models as util_models

class Transaction(models.Model):
    default_ship_to = models.ForeignKey(
        Location,
        verbose_name=_("Ship To"),
        related_name='default_ship_to',
        help_text=_("The default location that this transaction will "
                    "use as a ship-to-location."),
        on_delete=models.CASCADE,
        null=True
    )
    default_ship_from = models.ForeignKey(
        Location,
        verbose_name=_("Ship From"),
        related_name='default_ship_from',
        help_text=_("The default ship from location."),
        on_delete=models.CASCADE,
        null=True
    )
    default_possessing_party = models.ForeignKey(
        Company,
        verbose_name=_("Possessing Party"),
        related_name='default_possessing_party',
        help_text=_("The default possessing party if any."),
        on_delete=models.CASCADE,
        null=True
    )
    default_owning_party = models.ForeignKey(
        Company,
        related_name='default_owning_party',
        verbose_name=_("Owning Party"),
        help_text=_("The default owning party if any."),
        on_delete=models.CASCADE,
        null=True
    )
    users = models.ManyToManyField(get_user_model(),
                                   verbose_name=_("Users"),
                                   help_text=_("The users with rights to this"
                                               " transaction."),
                                   null=True)


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
