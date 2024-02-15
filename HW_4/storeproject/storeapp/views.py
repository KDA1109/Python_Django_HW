from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, get_object_or_404, redirect

import logging
from datetime import datetime, timedelta
from .models import Client, Product, Order
from .forms import ProductForm




def clients(request):

    all_clients = Client.objects.all()

    context = {'all_clients': all_clients}

    return render(request, "storeapp/clients.html", context)



def products(request):

    all_products = Product.objects.all()

    context = {'all_products': all_products}

    return render(request, "storeapp/products.html", context)

def orders(request):

    all_orders = Order.objects.all()

    context = {'all_orders': all_orders}

    return render(request, "storeapp/orders.html", context)



def client_orders(request, client_id):
    client = Client.objects.get(pk=client_id)

    period = request.GET.get('period')

    today = datetime.today().date()
    if period == '7':
        start_date = today - timedelta(days=7)
    elif period == '30':
        start_date = today - timedelta(days=30)
    elif period == '365':
        start_date = today - timedelta(days=365)
    else:
        start_date = None

    if start_date:
        client_orders = Order.objects.filter(client_id=client_id, date_ordered__gte=start_date).order_by('date_ordered')
    else:
        client_orders = Order.objects.filter(client_id=client_id).order_by('date_ordered')

    context = {'client': client, 'client_orders': client_orders}
    return render(request, 'storeapp/client_orders.html', context)


def update_product(request, product_id):
    product = get_object_or_404(Product, pk=product_id)

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            foto = form.cleaned_data['foto']
            fs = FileSystemStorage()
            fs.save(foto.name, foto)
            form.save()

    else:

        form = ProductForm(instance=product)

    return render(request, 'storeapp/update_product.html', {'form': form})


