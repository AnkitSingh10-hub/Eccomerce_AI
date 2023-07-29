# Generated by Django 4.1.3 on 2023-07-08 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_remove_deliveryreport_user_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='deliveryreport',
            name='order',
        ),
        migrations.AddField(
            model_name='deliveryreport',
            name='reference_code',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='deliveryreport',
            name='username',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]