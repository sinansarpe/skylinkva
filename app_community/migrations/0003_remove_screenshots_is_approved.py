# Generated by Django 4.2.17 on 2024-12-23 06:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_community', '0002_rename_is_published_screenshots_is_published_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='screenshots',
            name='is_approved',
        ),
    ]