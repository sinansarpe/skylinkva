# Generated by Django 4.2.17 on 2024-12-15 22:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HQEvents',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Title')),
                ('date', models.DateField(verbose_name='Date')),
                ('type', models.CharField(blank=True, max_length=100, null=True, verbose_name='Type')),
                ('airports', models.CharField(blank=True, max_length=100, null=True, verbose_name='Airports')),
                ('description', models.TextField(blank=True, max_length=100, null=True, verbose_name='Description')),
                ('event_url', models.URLField(blank=True, max_length=100, null=True, verbose_name='Link')),
            ],
            options={
                'verbose_name': 'HQ Event',
                'verbose_name_plural': 'HQ Events',
            },
        ),
        migrations.CreateModel(
            name='TREvents',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Title')),
                ('date', models.DateField(verbose_name='Date')),
                ('type', models.CharField(blank=True, max_length=100, null=True, verbose_name='Type')),
                ('airports', models.CharField(blank=True, max_length=100, null=True, verbose_name='Airports')),
                ('description', models.TextField(blank=True, max_length=100, null=True, verbose_name='Description')),
                ('event_url', models.URLField(blank=True, max_length=100, null=True, verbose_name='Link')),
            ],
            options={
                'verbose_name': 'IVAOTR Event',
                'verbose_name_plural': 'IVAOTR Event',
            },
        ),
    ]
