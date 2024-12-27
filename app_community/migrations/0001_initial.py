# Generated by Django 4.2.17 on 2024-12-21 00:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Screenshots',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='members/uploads/screenshots/images', verbose_name='Screenshot')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('is_Published', models.BooleanField(default=False, verbose_name='is Published')),
                ('is_featured', models.BooleanField(default=False, verbose_name='is Featured')),
                ('is_mainpage', models.BooleanField(default=False, verbose_name='Published in Main')),
                ('username', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='screenshots', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
