from django.contrib.auth.models import AbstractUser
from django.db import models

from product_module.models import Product


# Create your models here.
class User(AbstractUser):
    address = models.CharField(max_length=300)
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    wish_list = models.ManyToManyField(Product, blank=True)

    def __str__(self):
        return self.username

    def total_orders(self):
        result = 0
        for order in self.order_set.all():
            result += order.price()
        return result
