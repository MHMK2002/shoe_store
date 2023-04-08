from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

from account_module.models import User
from product_module.models import Product


# Create your models here.
class Order(models.Model):
    red = 'red'
    green = 'green'
    blue = 'blue'
    black = 'black'
    white = 'white'

    COLOR_CHOICES = (
        (red, 'red'),
        (green, 'green'),
        (blue, 'blue'),
        (black, 'black'),
        (white, 'white'),
    )

    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    color = models.CharField(max_length=100, choices=COLOR_CHOICES, default='red')
    size = models.PositiveIntegerField(validators=[MinValueValidator(30), MaxValueValidator(50)])
    quantity = models.PositiveIntegerField(default=1)
    completed = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product.name + ' - ' + self.color

    def price(self):
        return self.product.price * self.quantity
