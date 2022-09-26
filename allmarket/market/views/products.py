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


def product_view(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'product.html', context={'product': product})


def add_category_view(request):
    if request.method == 'GET':
        return render(request, 'category_add.html')
    return added_category_prepare(request)


def added_category_prepare(request):
    products = Product.objects.all()
    category = Category.objects.create(
        category_name=request.POST.get("category_name"),
        category_description=request.POST.get("category_description")
    )
    print(f'Добавлена новая категория: {category.category_name}')
    return redirect('index')


def add_product_view(request):
    if request.method == 'GET':
        categories = Category.objects.all()
        context = {
            'categories': categories
        }
        return render(request, 'product_add.html', context)
    return added_product_prepare(request)


def added_product_prepare(request):
    post_category = request.POST.get("category")
    category = Category.objects.get(category_name=post_category)
    product = Product.objects.create(
        product_name=request.POST.get("product_name"),
        product_description=request.POST.get("product_description"),
        category=category,
        price=request.POST.get("price"),
        product_image=request.POST.get("product_image")
    )
    print(f'Добавлен новый продукт: {product.product_name}')
    return redirect(reverse('product_detail', kwargs={'pk': product.pk}))
