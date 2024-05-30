from django.core.management import BaseCommand
from catalog.models import Category, Product
import json
from django.db import connection


class Command(BaseCommand):

    @staticmethod
    def json_read_categories():
        with open('catalog_data.json', encoding='utf-8') as json_file:
            return json.load(json_file)

    @staticmethod
    def json_read_products():
        with open('product_data.json', encoding='utf-8') as json_file:
            return json.load(json_file)

    def handle(self, *args, **options):
        with connection.cursor() as cursor:
            cursor.execute('TRUNCATE TABLE catalog_category RESTART IDENTITY CASCADE;')

        # Удалите все категории
        Category.objects.all().delete()


        # Удалите все продукты
        Product.objects.all().delete()
        # Создайте списки для хранения объектов
        product_list = []
        category_list = []

        # Обходим все значения категорий из фиктсуры для получения информации об одном объекте
        for category in Command.json_read_categories():
            category_list.append(
                {"id": category['pk'], "name": category['fields']['name'],
                 "description": category['fields']['description']}
            )
        category_for_create = []
        for category_item in category_list:
            category_for_create.append(
                Category.objects.create(**category_item)
            )

        # Обходим все значения продуктов из фиктсуры для получения информации об одном объекте
        for product in Command.json_read_products():
            product_list.append(
                {"id": product['pk'], "name": product['fields']['name'],
                 "description": product['fields']['description'],
                 "image": product['fields']['image'],
                 "category": Category.objects.get(pk=product['fields']['category']),
                 "price": product['fields']['price'],
                 "created_at": product['fields']['created_at'],
                 "updated_at": product['fields']['updated_at']}
            )
        product_for_create = []
        for product_item in product_list:
            product_for_create.append(
                Product.objects.create(**product_item)
            )

        # Создаем объекты в базе с помощью метода bulk_create()
        Category.objects.bulk_create(category_for_create)
        Product.objects.bulk_create(product_for_create)