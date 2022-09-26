from django.contrib import admin

from market.models import Product, Category


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'category_name', 'category_description', 'state', 'created_at', 'changed_at')
    list_filter = ('id', 'category_name', 'category_description', 'state', 'created_at', 'changed_at')
    search_fields = ('id', 'category_name', 'category_description', 'state', 'created_at', 'changed_at')
    fields = ('id', 'category_name', 'category_description', 'state', 'created_at', 'changed_at')
    readonly_fields = ['id']


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'product_name', 'product_description', 'price', 'created_at', 'changed_at', 'category_id')
    list_filter = ('id', 'product_name', 'product_description', 'price', 'created_at', 'changed_at', 'category_id')
    search_fields = ('id', 'product_name', 'product_description', 'price', 'created_at', 'changed_at', 'category_id')
    fields = ('id', 'product_name', 'product_description', 'price', 'created_at', 'changed_at', 'category_id')
    readonly_fields = ['id']


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
