# Generated by Django 2.2.6 on 2019-12-03 20:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0020_auto_20191203_2104'),
    ]

    operations = [
        migrations.AlterField(
            model_name='design',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='users.UserProfile'),
        ),
    ]
