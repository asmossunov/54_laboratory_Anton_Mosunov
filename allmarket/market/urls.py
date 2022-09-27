from django.contrib import admin
from django.urls import path

from market.views.products import index_view, category_edit_view, delete_product, product_edit_view, product_view, add_category_view, add_product_view, categories_view, delete_category


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index_view, name='index'),
    path('products/', index_view, name='index'),
    path('products/<int:pk>/delete/', delete_product, name='product_delete'),
    path('categories/', categories_view, name='categories'),
    path('categories/<int:pk>/delete/', delete_category, name='category_delete'),
    path('categories/add/', add_category_view, name='category_add'),
    path('products/add/', add_product_view, name='product_add'),
    path('products/<int:pk>', product_view, name='product_detail'),
    path('categories/<int:pk>/edit/', category_edit_view, name='category_edit'),
    path('products/<int:pk>/edit/', product_edit_view, name='product_edit'),
]
