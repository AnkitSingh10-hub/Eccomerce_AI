# Generated by Django 4.0.4 on 2022-10-25 22:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0028_order_ref_code_order_refund_granted_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='unit_price',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='unit_total_price',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
