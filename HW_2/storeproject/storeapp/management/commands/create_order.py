from django.core.management.base import BaseCommand
from storeapp.models import Order, Client, Product


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        client = Client.objects.get(id=4)
        product = Product.objects.get(id=1)
        order = Order(
            client_id=client,
            total_price=5000,
        )
        order.save()
        order.product_id.set([product])

