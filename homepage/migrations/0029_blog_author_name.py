# Generated by Django 4.2.2 on 2023-08-13 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0028_blog_ticket'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='author_name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]