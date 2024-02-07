from django.core.management.base import BaseCommand
from storeapp.models import Product


class Command(BaseCommand):
    help = "Add product."

    def handle(self, *args, **kwargs):
        product = Product(
            product_name='Пальто',
            description='женское, желтое',
            price='4500',
            product_amount='15'
        )
        product.save()

