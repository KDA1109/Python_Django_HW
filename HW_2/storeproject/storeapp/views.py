from django.shortcuts import render
from django.http import HttpResponse
from .models import Client, Product, Order
import pandas as pd



def clients(request):

    all_clients = Client.objects.all()


    data = {
        'ID': [client.id for client in all_clients],
        'Имя': [client.name for client in all_clients],
        'Почта': [client.email for client in all_clients],
        'Номер телефона': [client.phone_number for client in all_clients],
        'Адрес клиента': [client.address for client in all_clients],
        'Дата регистрации': [client.registration_date for client in all_clients],
    }
    df = pd.DataFrame(data)


    table_html = df.to_html(index=False)

    return HttpResponse(table_html)



def products(request):

    all_products = Product.objects.all()

    data = {
        'ID': [product.id for product in all_products],
        'Название': [product.product_name for product in all_products],
        'Описание': [product.description for product in all_products],
        'Цена': [product.price for product in all_products],
        'Количество': [product.product_amount for product in all_products],
        'Дата регистрации': [product.product_reg_date for product in all_products],
    }
    df = pd.DataFrame(data)

    table_html = df.to_html(index=False)

    return HttpResponse(table_html)


def orders(request):

    all_orders = Order.objects.all()

    data = {
        'ID': [order.id for order in all_orders],
        'ID Клиента': [order.client_id_id for order in all_orders],
        'ID товара': [order.product_id for order in all_orders],
        'Общая стоимость заказа': [order.total_price for order in all_orders],
        'Дата заказа': [order.date_ordered for order in all_orders],

    }
    df = pd.DataFrame(data)

    table_html = df.to_html(index=False)

    return HttpResponse(table_html)