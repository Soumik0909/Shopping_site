from django.apps import AppConfig
from django.template.defaultfilters import default


class ProductsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'products'
