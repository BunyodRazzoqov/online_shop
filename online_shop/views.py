from django.http import HttpResponse
from django.shortcuts import render

from online_shop.models import Product, Category


# Create your views here.


def product_list(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'online_shop/home.html', context)


def categories(request):
    category_list = Category.objects.all()
    context = {'categories': category_list}
    return render(request, 'online_shop/home.html', context)


def product_detail(request, product_id):
    try:
        product = Product.objects.get(id=product_id)
        context = {'product': product}
        return render(request, 'online_shop/detail.html', context)
    except:
        return HttpResponse('No such product', status=404)
