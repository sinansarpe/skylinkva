from django.apps import AppConfig


class AppDatabaseConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app_database'
    verbose_name = 'Airline Database'
