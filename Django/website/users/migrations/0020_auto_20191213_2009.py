# Generated by Django 2.2.6 on 2019-12-13 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0019_userprofile_actived_artist_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='actived_artist_date',
            field=models.DateTimeField(blank=True),
        ),
    ]
