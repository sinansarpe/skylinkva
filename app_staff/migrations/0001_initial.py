# Generated by Django 4.2.17 on 2024-12-25 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UploadLivery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.SmallIntegerField(default=1, verbose_name='Order')),
                ('title', models.CharField(max_length=100, verbose_name='Title')),
                ('livery', models.FileField(upload_to='uploads/airline/livery', verbose_name='Livery File')),
                ('description', models.TextField(blank=True, help_text='Additional information if required', null=True, verbose_name='Description')),
                ('upload_date', models.DateField(auto_now_add=True, verbose_name='Uploaded at')),
                ('livery_image', models.ImageField(blank=True, null=True, upload_to='uploads/airline/livery/image', verbose_name='Livery Image')),
            ],
            options={
                'verbose_name': 'Aircraft Livery Upload',
                'verbose_name_plural': 'Aircraft Livery Uploads',
            },
        ),
    ]
