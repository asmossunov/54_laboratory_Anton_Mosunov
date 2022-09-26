from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

from market.models import Category, Product
from market.models import categories

def index_view(request):
    if request.method == 'GET':
        products = Product.objects.all()
        context = {
            'products': products,
        }
        return render(request, 'index.html', context)


def product_view(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'task.html', context={'product': product})


def add_category_view(request):
    if request.method == 'GET':
        return render(request, 'add_task.html')
    return added_category_prepare(request)


def added_category_prepare(request):
    category = Category.objects.create(
        category_name=request.POST.get("category_name"),
        category_description=request.POST.get("category_description")
    )
    categories.append(category.category_name)
    print(f'Добавлена новая категория: {category.category_name}')
    return redirect('index')


