from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated

from account_module.models import User
from order_module.models import Order
from order_module.serializers import OrderSerializer
from rest_framework.parsers import JSONParser

class OrderListView(ListAPIView):
    model = Order
    serializer_class = OrderSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        completed = self.kwargs.get('completed') == 'True'
        queryset = self.model.objects.filter(completed=completed).all()
        return queryset.order_by('-date_created')


class OrderAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        user: User = request.user
        order = user.order_set.filter(pk=pk).first()
        if order is None:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = OrderSerializer(order)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = OrderSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        user: User = request.user
        order = user.order_set.get(pk=pk)
        serializer = OrderSerializer(order, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk=None):
        user: User = request.user
        if pk is None:
            orders = user.order_set.all()
            for order in orders:
                order.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            order = user.order_set.filter(pk=pk).first()
            if order is None:
                return Response(status=status.HTTP_404_NOT_FOUND)

            order.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
