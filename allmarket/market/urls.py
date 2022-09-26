from django.contrib import admin
from django.urls import path

from market.views.tasks import index_view, product_view, add_category_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index_view, name='index'),
    # path('tasks/confirmation/<int:pk>', confirmation_view, name='delete_confirmation'),
    path('categories/add/', add_category_view, name='category_add'),
    path('products/<int:pk>', product_view, name='product_detail'),
    # path('edit/', task_view, name='task_edit'),
    # path('tasks/edit/<int:pk>', task_edit_view, name='task_edit'),
]
