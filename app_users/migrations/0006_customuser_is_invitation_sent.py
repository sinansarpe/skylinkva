# Generated by Django 4.2.17 on 2024-12-23 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_users', '0005_customuser_age'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='is_invitation_sent',
            field=models.BooleanField(default=False, verbose_name='Invitation Sent'),
        ),
    ]
