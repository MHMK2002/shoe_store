from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from account_module.models import User
from product_module.models import Product
from product_module.serializers import ProductSerializer


class ProductView(APIView):
    def get(self, request, pk=None):
        if pk is None:
            products = Product.objects.all()
            serializer = ProductSerializer(products, many=True)
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        else:
            product = Product.objects.filter(pk=pk).first()
            serializer = ProductSerializer(product, many=False)
            return Response(data=serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def put(self, request, pk):
        product = Product.objects.filter(pk=pk).first()
        if product is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = ProductSerializer(product, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk=None):
        if pk is None:
            products = Product.objects.all()
            for product in products:
                product.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)

        product = Product.objects.filter(pk=pk)
        if product is None:
            return Response(status=status.HTTP_404_NOT_FOUND)

        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class WishListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk=None):
        user: User = request.user
        if pk is None:
            product = user.wish_list.filter(pk=pk).first()

            if product is None:
                return Response(data={
                    'isWishList': False,
                })
            else:
                return Response(data={
                    'isWishList': True,
                })
        else:
            wish_list = user.wish_list.all()
            serializer = ProductSerializer(wish_list, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, pk):
        user: User = request.user
        product = user.wish_list.filter(pk=pk).first()

        if product is None:
            product = Product.objects.filter(pk=pk).first()
            if product is None:
                return Response(status=status.HTTP_404_NOT_FOUND)
            user.wish_list.add(product)
            user.save()
            return Response(data={
                'isWishList': True,
            })
        else:
            product.delete()
            return Response(data={
                'isWishList': False,
            })
