# Generated by Django 2.2.6 on 2019-11-23 14:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('art', '0028_auto_20191117_2142'),
        ('products', '0009_auto_20191119_1412'),
    ]

    operations = [
        migrations.CreateModel(
            name='Design',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coordinate_left', models.IntegerField()),
                ('coordinate_top', models.IntegerField()),
                ('height', models.IntegerField()),
                ('art', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='art.Artwork')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.Product')),
            ],
        ),
    ]