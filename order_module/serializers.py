from rest_framework import serializers

from order_module.models import Order


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        field = '__all__'
