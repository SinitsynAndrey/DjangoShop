from django.core.management.base import BaseCommand
from mainapp.models import Products, Products_categories
from authapp.models import ShopUser


import json

JSON_PATH = 'mainapp/json/'

def load_from_json(file_name):
    with open(f'{JSON_PATH}{file_name}.json', 'r', encoding="utf-8") as json_file:
        return json.load(json_file)

class Command(BaseCommand):

    def handle(self, *args, **options):
        categories = load_from_json('categories')

        Products_categories.objects.all().delete()
        for category in categories:
            new_category = Products_categories(**category)
            new_category.save()

        products = load_from_json('products')

        Products.objects.all().delete()
        for product in products:
            category_name = product["category"]
            _category = Products_categories.objects.get(name=category_name)
            product['category'] = _category
            new_product = Products(**product)
            new_product.save()

        super_user = ShopUser.objects.create_superuser('django', password='geekbrains', age=32)