# Generated by Django 2.2.6 on 2019-11-25 20:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0012_auto_20191125_2124'),
    ]

    operations = [
        migrations.AlterField(
            model_name='design',
            name='rotation',
            field=models.CharField(default='matrix(1, 0, 0, 1, 0, 0)', max_length=30),
        ),
    ]
