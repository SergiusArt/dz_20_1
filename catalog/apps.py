from django.apps import AppConfig


# Описание приложения Catalog
class CatalogConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'catalog'
    verbose_name = 'Каталог'
