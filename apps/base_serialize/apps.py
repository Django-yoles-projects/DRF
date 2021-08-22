from django.apps import AppConfig


class BaseSerializeConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.base_serialize'
