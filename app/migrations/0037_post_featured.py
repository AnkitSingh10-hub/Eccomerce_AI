# Generated by Django 4.0.4 on 2022-10-29 19:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0036_author_blogcategory_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='featured',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
    ]
