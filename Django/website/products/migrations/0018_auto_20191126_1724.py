# Generated by Django 2.2.6 on 2019-11-26 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0017_design_frame_border_radius'),
    ]

    operations = [
        migrations.AlterField(
            model_name='design',
            name='frame_border_radius',
            field=models.IntegerField(default=0),
        ),
    ]