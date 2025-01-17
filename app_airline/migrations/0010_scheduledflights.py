# Generated by Django 4.2.17 on 2024-12-17 20:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_airline', '0009_aircraft_engine_type_aircraft_max_passengers'),
    ]

    operations = [
        migrations.CreateModel(
            name='ScheduledFlights',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('flight_number', models.SmallIntegerField(help_text='Number only: 102', verbose_name='Flight Number')),
                ('callsign', models.CharField(help_text='3 Chars only : 3EG', max_length=3, verbose_name='Callsign')),
                ('departure', models.CharField(help_text='City and IATA: Bodrum/BJV', max_length=50, verbose_name='Departure Airport')),
                ('arrival', models.CharField(help_text='City and IATA: Ankara/ESB', max_length=50, verbose_name='Arrival Airport')),
                ('aircraft', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app_airline.aircraft', verbose_name='Assigned Aircraft')),
            ],
            options={
                'verbose_name': 'Scheduled Flight (Everyday)',
                'verbose_name_plural': 'Scheduled Flights (Everyday)',
            },
        ),
    ]
