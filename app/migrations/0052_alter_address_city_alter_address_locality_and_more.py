# Generated by Django 4.0.4 on 2022-11-06 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0051_alter_address_city_alter_address_locality_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='city',
            field=models.CharField(max_length=150, verbose_name='City'),
        ),
        migrations.AlterField(
            model_name='address',
            name='locality',
            field=models.CharField(max_length=150, verbose_name='Nearest Location'),
        ),
        migrations.AlterField(
            model_name='address',
            name='state',
            field=models.CharField(max_length=150, verbose_name='State'),
        ),
    ]
