# Generated by Django 4.2.17 on 2024-12-15 22:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_events', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hqevents',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='trevents',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='Description'),
        ),
    ]