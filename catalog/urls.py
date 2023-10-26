from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import ContactsView, IndexView, ProductListView, ProductCreateView, ProductUpdateView, CategoryCreateView, ProductDeleteView

# Конфигурационное имя приложения
app_name = CatalogConfig.name

# Ссылки на страницы приложения Catalog
urlpatterns = [
    # Главная страница
    path('', IndexView.as_view(), name='start_form'),
    # Страница контактов
    path('contacts/', ContactsView.as_view(), name='contacts'),
    # Список товаров
    path('products/<int:pk>/', ProductListView.as_view(), name='product_list'),
    # Создание товара
    path('products/create/', ProductCreateView.as_view(), name='create_product'),
    # Редактирование товара
    path('products/update/<int:pk>/', ProductUpdateView.as_view(), name='update_product'),
    # Удаление товара
    path('products/delete/<int:pk>/', ProductDeleteView.as_view(), name='delete_product'),
    # Создание категории
    path('category/create/', CategoryCreateView.as_view(), name='create_category'),
]