from django.shortcuts import render
from mainapp.models import Products_categories, Products
from django.shortcuts import get_object_or_404
from basketapp.models import Basket
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import random

# Create your views here.

def main(request):
    content = {
        'title': 'Магазин',
        'products': Products.objects.all()[:4],
    }
    return render(request, 'mainapp/index.html', context=content)

def contact(request):
    content = {
        'title': 'Контанты',
    }
    return render(request, 'mainapp/contact.html', context=content)


def get_hot_product():
    hot_product = random.sample(list(Products.objects.all()), 1)[0]
    return hot_product


def get_same_products(hot_product):
    same_products = Products.objects.filter(category=hot_product.category).exclude(pk = hot_product.pk)[:3]
    return same_products


def products(request, pk=None):
    title = 'Продукты'
    links_menu = Products_categories.objects.filter(is_active=True)

    if pk is not None:
        if pk == 0:
            products = Products.objects.all().order_by('price')
            category = {'name': 'все',
                        'pk': 0}
        else:
            category = get_object_or_404(Products_categories, pk=pk)
            products = Products.objects.filter(category__pk=pk).order_by('price')

        page = request.GET.get('p', 1)
        paginator = Paginator(products, 2)
        try:
            product_paginator = paginator.page(page)
        except PageNotAnInteger:
            product_paginator = paginator.page(1)
        except EmptyPage:
            product_paginator = paginator.page(paginator.num_pages)

        content = {
            'title': title,
            'links_menu': links_menu,
            'category': category,
            'products': product_paginator,
        }
        return render(request, 'mainapp/products_list.html', context=content)

    hot_product = get_hot_product()
    same_product = get_same_products(hot_product)

    content = {
        'hot_product': hot_product,
        'same_products': same_product,
        'title': title,
        'links_menu': links_menu,
    }

    return render(request, 'mainapp/products.html', context=content)

def product(request, pk):
    title = Products.objects.get(pk=pk).name

    content = {
        'title': title,
        'links_menu': Products_categories.objects.all(),
        'product': get_object_or_404(Products, pk=pk),
    }

    return render(request, 'mainapp/product.html', context=content)

