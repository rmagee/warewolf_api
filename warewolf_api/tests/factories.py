from quartet_masterdata import models
from warewolf_api.models import Transaction
from django.contrib.auth import get_user_model
from EPCPyYes.core.v1_2 import CBV, events
import factory
from factory import BUILD_STRATEGY


class LocationTypeFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.LocationType

    identifier = 'BSS'
    description = 'Baseball Stadium'


class LocationFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Location
        django_get_or_create = ('GLN13', 'SGLN')

    GLN13 = '3055551234577'
    SGLN = 'urn:epc:id:sgln:305555.333333.0'
    name = "Headquarters"
    address1 = 'One Citizens Bank Way'
    country = 'US'
    city = 'Philadelphia'
    state_province = 'PA'
    postal_code = '19148'
    latitude = '39.906098'
    longitude = '-75.165733'
    location_type = factory.SubFactory(LocationTypeFactory)

class LocationFieldFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.LocationField

    name = 'Internal Code'
    value = 'PL72'
    description = 'Internal plant code #72.'
    location = factory.SubFactory(LocationFactory)


class LocationIdentifierFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.LocationIdentifier

    identifier = 'urn:epc:id:sgln:305555.777777.1'
    identifier_type = 'SGLN'
    description = 'First Base'
    location = factory.SubFactory(LocationFactory)


class CompanyTypeFactory(factory.DjangoModelFactory):
    class Meta:
        model = models.CompanyType

    identifier = 'MANU'
    description = 'Manufacturer'


class CompanyFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Company
        django_get_or_create = ('GLN13', 'SGLN')

    gs1_company_prefix = '234156'
    company_type = factory.SubFactory(CompanyTypeFactory)
    GLN13 = '3055551234556'
    SGLN = 'urn:epc:id:sgln:305555.123456.7'
    name = "Headquarters"
    address1 = 'One Citizens Bank Way'
    country = 'US'
    city = 'Philadelphia'
    state_province = 'PA'
    postal_code = '19148'
    latitude = '39.906098'
    longitude = '-75.165733'


class TradeItemFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.TradeItem

    company = factory.SubFactory(CompanyFactory)
    country_of_origin = 'US'
    drained_weight = None
    gross_weight = 10.5
    gross_weight_uom = 'LBR'
    net_weight = 10
    net_weight_uom = 'LBR'
    GTIN14 = '12341234123422'
    NDC = '1234-1234-22'
    NDC_pattern = '4-4-2'
    additional_id = '45039-33'
    additional_id_typecode = 'GST'
    description_short = 'Supressitol'
    dosage_form_type = 'PILL'
    functional_name = 'Widget'
    manufacturer_name = 'Acme Corp.'
    net_content_description = '600 grams'
    label_description = 'Supressitol Tablets: 10 grams of suppression.'
    regulated_product_name = 'Supressitoxide Carbonite'
    strength_description = '100mg'
    trade_item_description = 'Supressitol Brand Suppression Tablets'


class TradeItemFieldFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.TradeItemField

    trade_item = factory.SubFactory(TradeItemFactory)
    name = 'MATNO'
    value = '32423-33-777'
    description = 'SAP Internal Material Number'


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = get_user_model()

    username = 'testuser'
    password = 'testpassword'
    email = 'test@local.local'
    is_superuser = True


class TransactionFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Transaction

    name = 'Simple Shipping'
    icon = 'Check'
    default_ship_from = LocationFactory()
    print(
        '**************  creating the second location...'
    )
    default_ship_to = LocationFactory(
        GLN13='3055551234554',
        SGLN='urn:epc:id:sgln:305555.222222.2',
        name="There",
        address1='Not here but there.'
    )
    default_possessing_party = CompanyFactory()
    default_owning_party = CompanyFactory(
        SGLN='urn:epc:id:sgln:305555.999999.0',
        gs1_company_prefix='234127',
        company_type=factory.SubFactory(CompanyTypeFactory),
        GLN13='3055551234555',
        name="Headquarters"
    )
    auto_disaggregate = True
    event_type = 'OBJECT'
    biz_step = CBV.BusinessSteps.shipping.value
    disposition = CBV.Disposition.in_transit
    action = events.Action.add.value


class UserTransactionFactory(UserFactory):
    users = factory.RelatedFactory(TransactionFactory, 'users',
                                   transaction__name='Simple Shipping')
