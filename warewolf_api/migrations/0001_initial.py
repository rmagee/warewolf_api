# Generated by Django 2.2.3 on 2019-08-12 16:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('quartet_masterdata', '0006_auto_20190812_1630'),
    ]

    operations = [
        migrations.CreateModel(
            name='BarcodeCache',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('barcode', models.CharField(help_text='The barcode that was queried.', max_length=200, verbose_name='Barcode')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, help_text='Create date.', verbose_name='Created')),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, help_text='Unique ID', primary_key=True, serialize=False, verbose_name='Unique ID')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='When this record was created.', verbose_name='Created')),
                ('modified', models.DateTimeField(auto_now=True, help_text='When this record was last modified.', verbose_name='Modified')),
                ('event_time', models.DateTimeField(db_index=True, editable=False, help_text='The date and time at which the EPCIS Capturing Application asserts the event occurred.', verbose_name='Event Time')),
                ('event_timezone_offset', models.CharField(default='+00:00', help_text='The time zone offset in effect at the time and place the event occurred, expressed as an offset from UTC', max_length=6, null=True, verbose_name='Event Timezone Offset')),
                ('record_time', models.DateTimeField(default=django.utils.timezone.now, help_text='The date and time at which this event was recorded by an EPCIS Repository.', null=True, verbose_name='Record Time')),
                ('event_id', models.CharField(db_index=True, default=uuid.uuid4, help_text='An identifier for this event as specified by the capturing application, globally unique across all events other than error declarations. Not to be confused with the unique id/primary key for events within a database.', max_length=150, null=True, verbose_name='Event ID')),
                ('action', models.CharField(choices=[('ADD', 'Add'), ('OBSERVE', 'Observe'), ('DELETE', 'Delete')], help_text='How this event relates to the lifecycle of the EPCs named in this event.', max_length=10, verbose_name='Action')),
                ('biz_step', models.CharField(blank=True, choices=[('urn:epcglobal:cbv:bizstep:accepting', 'urn:epcglobal:cbv:bizstep:accepting'), ('urn:epcglobal:cbv:bizstep:arriving', 'urn:epcglobal:cbv:bizstep:arriving'), ('urn:epcglobal:cbv:bizstep:assembling', 'urn:epcglobal:cbv:bizstep:assembling'), ('urn:epcglobal:cbv:bizstep:collecting', 'urn:epcglobal:cbv:bizstep:collecting'), ('urn:epcglobal:cbv:bizstep:commissioning', 'urn:epcglobal:cbv:bizstep:commissioning'), ('urn:epcglobal:cbv:bizstep:consigning', 'urn:epcglobal:cbv:bizstep:consigning'), ('urn:epcglobal:cbv:bizstep:creating_class_instance', 'urn:epcglobal:cbv:bizstep:creating_class_instance'), ('urn:epcglobal:cbv:bizstep:cycle_counting', 'urn:epcglobal:cbv:bizstep:cycle_counting'), ('urn:epcglobal:cbv:bizstep:decommissioning', 'urn:epcglobal:cbv:bizstep:decommissioning'), ('urn:epcglobal:cbv:bizstep:departing', 'urn:epcglobal:cbv:bizstep:departing'), ('urn:epcglobal:cbv:bizstep:destroying', 'urn:epcglobal:cbv:bizstep:destroying'), ('urn:epcglobal:cbv:bizstep:disassembling', 'urn:epcglobal:cbv:bizstep:disassembling'), ('urn:epcglobal:cbv:bizstep:dispensing', 'urn:epcglobal:cbv:bizstep:dispensing'), ('urn:epcglobal:cbv:bizstep:entering_exit', 'urn:epcglobal:cbv:bizstep:entering_exit'), ('urn:epcglobal:cbv:bizstep:ingholding', 'urn:epcglobal:cbv:bizstep:ingholding'), ('urn:epcglobal:cbv:bizstep:inspecting', 'urn:epcglobal:cbv:bizstep:inspecting'), ('urn:epcglobal:cbv:bizstep:installing', 'urn:epcglobal:cbv:bizstep:installing'), ('urn:epcglobal:cbv:bizstep:killing', 'urn:epcglobal:cbv:bizstep:killing'), ('urn:epcglobal:cbv:bizstep:loading', 'urn:epcglobal:cbv:bizstep:loading'), ('urn:epcglobal:cbv:bizstep:other', 'urn:epcglobal:cbv:bizstep:other'), ('urn:epcglobal:cbv:bizstep:packing', 'urn:epcglobal:cbv:bizstep:packing'), ('urn:epcglobal:cbv:bizstep:picking', 'urn:epcglobal:cbv:bizstep:picking'), ('urn:epcglobal:cbv:bizstep:receiving', 'urn:epcglobal:cbv:bizstep:receiving'), ('urn:epcglobal:cbv:bizstep:removing', 'urn:epcglobal:cbv:bizstep:removing'), ('urn:epcglobal:cbv:bizstep:repackaging', 'urn:epcglobal:cbv:bizstep:repackaging'), ('urn:epcglobal:cbv:bizstep:repairing', 'urn:epcglobal:cbv:bizstep:repairing'), ('urn:epcglobal:cbv:bizstep:replacing', 'urn:epcglobal:cbv:bizstep:replacing'), ('urn:epcglobal:cbv:bizstep:reserving', 'urn:epcglobal:cbv:bizstep:reserving'), ('urn:epcglobal:cbv:bizstep:retail_selling', 'urn:epcglobal:cbv:bizstep:retail_selling'), ('urn:epcglobal:cbv:bizstep:shipping', 'urn:epcglobal:cbv:bizstep:shipping'), ('urn:epcglobal:cbv:bizstep:staging_outbound', 'urn:epcglobal:cbv:bizstep:staging_outbound'), ('urn:epcglobal:cbv:bizstep:stock_taking', 'urn:epcglobal:cbv:bizstep:stock_taking'), ('urn:epcglobal:cbv:bizstep:stocking', 'urn:epcglobal:cbv:bizstep:stocking'), ('urn:epcglobal:cbv:bizstep:storing', 'urn:epcglobal:cbv:bizstep:storing'), ('urn:epcglobal:cbv:bizstep:transporting', 'urn:epcglobal:cbv:bizstep:transporting'), ('urn:epcglobal:cbv:bizstep:unloading', 'urn:epcglobal:cbv:bizstep:unloading'), ('urn:epcglobal:cbv:bizstep:unpacking', 'urn:epcglobal:cbv:bizstep:unpacking'), ('urn:epcglobal:cbv:bizstep:void_shipping', 'urn:epcglobal:cbv:bizstep:void_shipping')], help_text='The business step of which this event was a part.', max_length=150, null=True, verbose_name='Business Step')),
                ('disposition', models.CharField(blank=True, choices=[('urn:epcglobal:cbv:disp:active', 'urn:epcglobal:cbv:disp:active'), ('urn:epcglobal:cbv:disp:container_closed', 'urn:epcglobal:cbv:disp:container_closed'), ('urn:epcglobal:cbv:disp:damaged', 'urn:epcglobal:cbv:disp:damaged'), ('urn:epcglobal:cbv:disp:destroyed', 'urn:epcglobal:cbv:disp:destroyed'), ('urn:epcglobal:cbv:disp:dispensed', 'urn:epcglobal:cbv:disp:dispensed'), ('urn:epcglobal:cbv:disp:disposed', 'urn:epcglobal:cbv:disp:disposed'), ('urn:epcglobal:cbv:disp:encoded', 'urn:epcglobal:cbv:disp:encoded'), ('urn:epcglobal:cbv:disp:expired', 'urn:epcglobal:cbv:disp:expired'), ('urn:epcglobal:cbv:disp:in_progress', 'urn:epcglobal:cbv:disp:in_progress'), ('urn:epcglobal:cbv:disp:in_transit', 'urn:epcglobal:cbv:disp:in_transit'), ('urn:epcglobal:cbv:disp:inactive', 'urn:epcglobal:cbv:disp:inactive'), ('urn:epcglobal:cbv:disp:no_pedigree_match', 'urn:epcglobal:cbv:disp:no_pedigree_match'), ('urn:epcglobal:cbv:disp:non_sellable_other', 'urn:epcglobal:cbv:disp:non_sellable_other'), ('urn:epcglobal:cbv:disp:partially_dispensed', 'urn:epcglobal:cbv:disp:partially_dispensed'), ('urn:epcglobal:cbv:disp:recalled', 'urn:epcglobal:cbv:disp:recalled'), ('urn:epcglobal:cbv:disp:reserved', 'urn:epcglobal:cbv:disp:reserved'), ('urn:epcglobal:cbv:disp:retail_sold', 'urn:epcglobal:cbv:disp:retail_sold'), ('urn:epcglobal:cbv:disp:returned', 'urn:epcglobal:cbv:disp:returned'), ('urn:epcglobal:cbv:disp:sellable_accessible', 'urn:epcglobal:cbv:disp:sellable_accessible'), ('urn:epcglobal:cbv:disp:sellable_not_accessible', 'urn:epcglobal:cbv:disp:sellable_not_accessible'), ('urn:epcglobal:cbv:disp:stolen', 'urn:epcglobal:cbv:disp:stolen'), ('urn:epcglobal:cbv:disp:unknown', 'urn:epcglobal:cbv:disp:unknown')], help_text='The business condition of the objects associated with the EPCs, presumed to hold true until contradicted by a subsequent event..', max_length=150, null=True, verbose_name='Disposition')),
                ('read_point', models.CharField(blank=True, help_text='The read point at which the event took place.', max_length=150, null=True, verbose_name='Read Point')),
                ('biz_location', models.CharField(blank=True, help_text='The business location where the objects associated with the EPCs may be found, until contradicted by a subsequent event.', max_length=150, null=True, verbose_name='Business Location')),
                ('name', models.CharField(help_text='The user-friendly name of this transaction.', max_length=200, verbose_name='Name')),
                ('description', models.CharField(blank=True, help_text='A brief description of this transaction', max_length=500, null=True, verbose_name='Brief Description')),
                ('default_owning_party', models.ForeignKey(help_text='The default owning party if any.', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='default_owning_party', to='quartet_masterdata.Company', verbose_name='Owning Party')),
                ('default_possessing_party', models.ForeignKey(help_text='The default possessing party if any.', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='default_possessing_party', to='quartet_masterdata.Company', verbose_name='Possessing Party')),
                ('default_ship_from', models.ForeignKey(help_text='The default ship from location.', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='default_ship_from', to='quartet_masterdata.Location', verbose_name='Ship From')),
                ('default_ship_to', models.ForeignKey(help_text='The default location that this transaction will use as a ship-to-location.', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='default_ship_to', to='quartet_masterdata.Location', verbose_name='Ship To')),
                ('users', models.ManyToManyField(help_text='The users with rights to this transaction.', null=True, to=settings.AUTH_USER_MODEL, verbose_name='Users')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
