# Generated by Django 2.2.6 on 2019-10-30 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_order_product_wish'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='user',
            field=models.ForeignKey(on_delete=models.SET('unknown'), to='users.UserProfile'),
        ),
        migrations.AlterField(
            model_name='wish',
            name='user',
            field=models.ForeignKey(on_delete=models.SET('unknown'), to='users.UserProfile'),
        ),
    ]