# Generated by Django 2.2.3 on 2019-11-06 17:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('warewolf_api', '0008_auto_20191011_2140'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='event_time',
            field=models.DateTimeField(default=datetime.datetime(2019, 11, 6, 17, 55, 0, 221479), help_text='The date this transaction was initially created.', verbose_name='Created Date'),
        ),
    ]
