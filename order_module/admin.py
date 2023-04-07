from django.contrib import admin

from order_module.models import Order


# Register your models here.
@admin.register(Order)
class OrderAdminModel(admin.ModelAdmin):
    pass
