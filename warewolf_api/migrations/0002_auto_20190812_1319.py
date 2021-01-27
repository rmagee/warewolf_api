# Generated by Django 2.2.3 on 2019-08-12 18:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('quartet_output', '0004_auto_20190725_1122'),
        ('warewolf_api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='authentication_info',
            field=models.ForeignKey(help_text='The Authentication Info to use when sending transaction data.', null=True, on_delete=django.db.models.deletion.SET_NULL, to='quartet_output.AuthenticationInfo', verbose_name='Authentication Info'),
        ),
        migrations.AddField(
            model_name='transaction',
            name='auto_decommission_parent',
            field=models.BooleanField(default=False, help_text='When picking an item from a parent, should the parent be automagically decommissioned and the rest of the children freed up.', verbose_name='Auto Decommission Parent'),
        ),
        migrations.AddField(
            model_name='transaction',
            name='auto_disaggregate',
            field=models.BooleanField(default=False, help_text='Whether or not this transaction should automagically disaggregate items that are being packed (when applicable).', verbose_name='Auto Disaggregate'),
        ),
        migrations.AddField(
            model_name='transaction',
            name='end_point',
            field=models.ForeignKey(help_text='A prtocol-specific endpoint defining where any output data will be sent.', on_delete=django.db.models.deletion.PROTECT, to='quartet_output.EndPoint', verbose_name='End Point'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='transaction',
            name='ilmd_field',
            field=models.CharField(choices=[('bestBeforeDate', 'bestBeforeDate'), ('countryOfOrigin', 'countryOfOrigin'), ('farmList', 'farmList'), ('firstFreezeDate', 'firstFreezeDate'), ('growingMethodCode', 'growingMethodCode'), ('harvestEndDate', 'harvestEndDate'), ('harvestStartDate', 'harvestStartDate'), ('itemExpirationDate', 'itemExpirationDate'), ('sellByDate', 'sellByDate'), ('storageStateCode', 'storageStateCode'), ('additionalTradeItemIdentification', 'additionalTradeItemIdentification'), ('additionalTradeItemIdentificationTypeCode', 'additionalTradeItemIdentificationTypeCode'), ('countryOfOrigin', 'countryOfOrigin'), ('descriptionShort', 'descriptionShort'), ('dosageFormType', 'dosageFormType'), ('drainedWeight', 'drainedWeight'), ('functionalName', 'functionalName'), ('grossWeight ', 'grossWeight '), ('manufacturerOfTradeItemPartyName', 'manufacturerOfTradeItemPartyName'), ('netWeight ', 'netWeight '), ('labelDescription', 'labelDescription'), ('regulatedProductName', 'regulatedProductName'), ('strengthDescription', 'strengthDescription'), ('tradeItemDescription', 'tradeItemDescription'), ('countryOfOrigin', 'countryOfOrigin'), ('drainedWeight', 'drainedWeight'), ('grossWeight', 'grossWeight'), ('lotNumber', 'lotNumber'), ('netWeight', 'netWeight'), ('measurement', 'measurement'), ('measurementUnitCode', 'measurementUnitCode')], default=True, help_text='If scan by ILMD field is true, this will be the lookup field for serialized data to include in the message.', max_length=300, verbose_name='ILMD Field'),
        ),
        migrations.AddField(
            model_name='transaction',
            name='scan_ilmd',
            field=models.BooleanField(default=False, help_text='If true, users will not scan in serialized information but rather a lot/master data value. For example, ship by lot number.', verbose_name='Scan ILMD value'),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='users',
            field=models.ManyToManyField(help_text='The users with rights to this transaction.', to=settings.AUTH_USER_MODEL, verbose_name='Users'),
        ),
    ]