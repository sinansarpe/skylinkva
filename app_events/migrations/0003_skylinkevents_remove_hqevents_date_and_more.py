# Generated by Django 4.2.17 on 2024-12-17 22:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_events', '0002_alter_hqevents_description_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='SKYLinkEvents',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Title')),
                ('start_date', models.DateTimeField(blank=True, null=True, verbose_name='Start Date')),
                ('end_date', models.DateTimeField(blank=True, null=True, verbose_name='End Date')),
                ('type', models.CharField(blank=True, max_length=100, null=True, verbose_name='Type')),
                ('airports', models.CharField(blank=True, max_length=100, null=True, verbose_name='Airports')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Description')),
                ('event_url', models.URLField(blank=True, max_length=100, null=True, verbose_name='Link')),
            ],
        ),
        migrations.RemoveField(
            model_name='hqevents',
            name='date',
        ),
        migrations.RemoveField(
            model_name='trevents',
            name='date',
        ),
        migrations.AddField(
            model_name='hqevents',
            name='end_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='End Date'),
        ),
        migrations.AddField(
            model_name='hqevents',
            name='start_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Start Date'),
        ),
        migrations.AddField(
            model_name='trevents',
            name='end_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='End Date'),
        ),
        migrations.AddField(
            model_name='trevents',
            name='start_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Start Date'),
        ),
    ]
