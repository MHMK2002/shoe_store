from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


# Create your models here.
class ProductBrand(models.Model):
    name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='product_brand_logo')

    def __str__(self):
        return self.name


class ProductColor(models.Model):
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

    name = models.CharField(max_length=100, choices=COLOR_CHOICES, default=red)


class ProductSize:
    size = models.PositiveIntegerField(validators=[MinValueValidator(30), MaxValueValidator(50)])

class ProductImage(models.Model):
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='product_images')
    is_main = models.BooleanField(default=False)

    def __str__(self):
        return self.product.name + ' - image'


class Product(models.Model):
    name = models.CharField(max_length=100)
    brand = models.ForeignKey(ProductBrand, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    color = models.ForeignKey(ProductColor, on_delete=models.CASCADE)

    def __str__(self):
        return self.name



