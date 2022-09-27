from django.db import models
from django.db.models import TextChoices


class StateChoices(TextChoices):
    ACTIVE = 'ACTIVE'
    NOT_ACTIVE = 'NOT_ACTIVE'


class Category(models.Model):
    category_name = models.CharField(verbose_name='Название', max_length=100, null=False)
    category_description = models.TextField(verbose_name='Описание категории',
                                            max_length=3000, null=False, blank=False)
    state = models.CharField(verbose_name='Состояние', choices=StateChoices.choices,
                             max_length=100, default=StateChoices.ACTIVE)
    created_at = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)
    changed_at = models.DateTimeField(verbose_name='Дата изменения', auto_now=True)

    def __str__(self):
        return f'{self.category_name} {self.category_description}'


class Product(models.Model):
    product_name = models.CharField(verbose_name=' Товар', max_length=100, null=False)
    product_description = models.TextField(verbose_name='Описание товара',
                                           max_length=3000, null=False, blank=False)
    category = models.ForeignKey(verbose_name='Категория', to='market.Category', null=False, blank=False,
                                 related_name='products', on_delete=models.CASCADE)
    created_at = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)
    changed_at = models.DateTimeField(verbose_name='Дата изменения', auto_now=True)
    price = models.DecimalField(verbose_name='Стоимость', max_length=100, max_digits=15,
                                decimal_places=10)
    product_image = models.TextField(verbose_name='Изображение', max_length=3000,
                                     null=False, blank=False)

    def __str__(self):
        return f'{self.product_name} {self.category} {self.price} {self.product_description} {self.created_at}'
