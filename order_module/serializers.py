from rest_framework import serializers

from order_module.models import Order


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        exclude = ['date_created', 'user', 'completed']

    def create(self, validated_data):
        user = None
        print(self.context)
        print(self.context.get("request"))
        request = self.context.get("request")
        if request and hasattr(request, "user"):
            user = request.user
        order = Order.objects.create(user=user, **validated_data)
        return order
