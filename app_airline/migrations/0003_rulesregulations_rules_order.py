# Generated by Django 4.2.17 on 2024-12-16 21:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_airline', '0002_downloads_flightoperations_rankingsystem_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='rulesregulations',
            name='rules_order',
            field=models.SmallIntegerField(default=1, verbose_name='Order'),
        ),
    ]
