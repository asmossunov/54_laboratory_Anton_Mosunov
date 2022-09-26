from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

from market.models import Category, Product


def index_view(request):
    if request.method == 'GET':
        products = Product.objects.all()
        context = {
            'products': products,
        }
        return render(request, 'index.html', context)
