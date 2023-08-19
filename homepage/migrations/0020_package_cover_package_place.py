# Generated by Django 4.2.2 on 2023-08-07 15:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0019_alter_division_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='package',
            name='cover',
            field=models.ImageField(null=True, upload_to='packeage/'),
        ),
        migrations.AddField(
            model_name='package',
            name='place',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='homepage.place'),
        ),
    ]