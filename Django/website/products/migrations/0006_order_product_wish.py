# Generated by Django 2.2.6 on 2019-10-27 18:19

import datetime
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('art', '0012_artwork_comment'),
        ('products', '0005_auto_20191027_1912'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=60)),
                ('stock', models.IntegerField()),
                ('description', models.CharField(max_length=600)),
                ('price', models.IntegerField()),
                ('product_photo', models.ImageField(upload_to='')),
                ('upload_date', models.DateField(default=datetime.date.today, verbose_name='Date')),
            ],
        ),
        migrations.CreateModel(
            name='Wish',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wish_date', models.DateField(default=datetime.date.today, verbose_name='Date')),
                ('artwork', models.ForeignKey(on_delete=models.SET('deleted'), to='art.Artwork')),
                ('product', models.ForeignKey(on_delete=models.SET('deleted'), to='products.Product')),
                ('user', models.ForeignKey(on_delete=models.SET('unknown'), to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_date', models.DateField(default=datetime.date.today, verbose_name='Date')),
                ('artwork', models.ForeignKey(on_delete=models.SET('deleted'), to='art.Artwork')),
                ('product', models.ForeignKey(on_delete=models.SET('deleted'), to='products.Product')),
                ('user', models.ForeignKey(on_delete=models.SET('unknown'), to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]