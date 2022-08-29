from django.apps import AppConfig


class MainConfig(AppConfig):
    default_auto_field = 'django.mongo_db.models.BigAutoField'
    name = 'main'
