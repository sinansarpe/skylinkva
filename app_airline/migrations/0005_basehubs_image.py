# Generated by Django 4.2.17 on 2024-12-17 01:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_airline', '0004_rankingsystem_ranking_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='basehubs',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/airline/base-hubs/images', verbose_name='Airport Image'),
        ),
    ]
