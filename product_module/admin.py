from django.contrib import admin

from product_module.models import Product, ProductBrand, ProductImage


# Register your models here.
@admin.register(Product)
class ProductAdminModel(admin.ModelAdmin):
    pass


@admin.register(ProductBrand)
class ProductBrandAdminModel(admin.ModelAdmin):
    pass


@admin.register(ProductImage)
class ProductImageAdminModel(admin.ModelAdmin):
    pass
