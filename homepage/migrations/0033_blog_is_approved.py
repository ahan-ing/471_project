# Generated by Django 4.2.2 on 2023-08-17 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0032_package_duration'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='is_approved',
            field=models.BooleanField(default=False),
        ),
    ]
