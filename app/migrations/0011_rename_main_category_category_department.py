# Generated by Django 5.0.2 on 2024-02-23 22:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_rename_maincategory_department'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='main_category',
            new_name='department',
        ),
    ]
