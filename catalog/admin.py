from django.contrib import admin

from catalog.models import Product, Category


# Наименование продукта в админке
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'category')
    list_filter = ('category',)
    search_fields = ('name', 'description')
    verbose_name_plural = 'Продукты'


# Наименование категории в админке
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    verbose_name_plural = 'Категории'
