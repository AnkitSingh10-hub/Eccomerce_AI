# Generated by Django 4.0.4 on 2022-08-01 22:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0018_alter_cart_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='product',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='app.product', verbose_name='Product'),
            preserve_default=False,
        ),
    ]
