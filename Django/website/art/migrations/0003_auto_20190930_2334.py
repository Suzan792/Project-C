# Generated by Django 3.1.dev20190930082805 on 2019-09-30 21:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('art', '0002_painting_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='painting',
            name='photo',
            field=models.ImageField(default=123, upload_to='img'),
            preserve_default=False,
        ),
    ]
