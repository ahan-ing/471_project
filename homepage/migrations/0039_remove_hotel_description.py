# Generated by Django 4.2.2 on 2023-08-19 18:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0038_remove_hotel_address'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hotel',
            name='description',
        ),
    ]
