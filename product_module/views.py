from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from product_module.models import Product
from product_module.serializers import ProductSerializer


class ProductView(APIView):
    def get(self, request, id=None):
        if id is None:
            products = Product.objects.all()
            serializer = ProductSerializer(products, many=True)
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        else:
            product = Product.objects.filter(pk=id).first()
            serializer = ProductSerializer(product, many=False)
            return Response(data=serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def put(self, request, id):
        product = Product.objects.filter(id=id).first()
        if product is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = ProductSerializer(product, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id=None):
        if id is None:
            products = Product.objects.all()
            for product in products:
                product.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)

        product = Product.objects.filter(id=id)
        if product is None:
            return Response(status=status.HTTP_404_NOT_FOUND)

        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

