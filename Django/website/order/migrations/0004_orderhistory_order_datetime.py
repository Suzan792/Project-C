# Generated by Django 3.1 on 2019-12-13 17:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0003_remove_orderhistory_order_datetime'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderhistory',
            name='order_datetime',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='DateTime'),
        ),
    ]