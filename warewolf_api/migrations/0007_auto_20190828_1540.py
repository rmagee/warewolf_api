# Generated by Django 2.2.3 on 2019-08-28 15:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('warewolf_api', '0006_auto_20190814_1520'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='event_time',
            field=models.DateTimeField(default=datetime.datetime(2019, 8, 28, 15, 40, 41, 270237), help_text='The date this transaction was initially created.', verbose_name='Created Date'),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='icon',
            field=models.CharField(default='Check', help_text='The name of the Material-UI icon to display.', max_length=20, null=True, verbose_name='Icon'),
        ),
    ]
