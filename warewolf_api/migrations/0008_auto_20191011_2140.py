# Generated by Django 2.2.3 on 2019-10-11 21:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('warewolf_api', '0007_auto_20190828_1540'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='event_time',
            field=models.DateTimeField(default=datetime.datetime(2019, 10, 11, 21, 40, 7, 519916), help_text='The date this transaction was initially created.', verbose_name='Created Date'),
        ),
    ]