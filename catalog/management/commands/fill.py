from django.core.management import BaseCommand
from catalog.models import Category


class Command(BaseCommand):
    def handle(self, *args, **options):
        category_list = [
            {'name': 'компьютерный стол', 'description': 'широкий удобный стол'},
            {'name': 'компьютер', 'description': 'стационарный компьютер'},
            {'name': 'веб-камера', 'description': 'для компьютеров веб-камера'},
        ]

        # Очистка старых данных
        Category.objects.all().delete()

        # Создание и сохранение новых объектов категорий
        categories_for_create = [Category(**category) for category in category_list]
        Category.objects.bulk_create(categories_for_create)

        self.stdout.write(self.style.SUCCESS('Данные успешно добавлены.'))