from rest_framework import status, generics
from rest_framework.views import APIView
from .serializers import *
from rest_framework.response import Response
from .models import Product
import uuid
from rest_framework.permissions import IsAdminUser


class SignupApiView(generics.GenericAPIView):
    serializer_class = SignupSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {
                    "request_id": str(uuid.uuid4()),
                    "Message": 'User created successfully',
                    "User": serializer.data},
                status=status.HTTP_201_CREATED)
        return Response({"errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class ProductList(APIView):
    """
    Implementing productlist, add new products
    """

    def get(self, request, format=None):
        orders = Product.objects.all()
        serializer = ProductSerializer(orders, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        permission_classes = [IsAdminUser]
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,
                            status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SummaryOrder(APIView):
    """
    Implementing orderlist and add new orders
    """

    def get(self, request, format=None):
        orders = Orders.objects.all()
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)

class ProductOrder(APIView):
    def get(self, request):
        p_orders = ProductOrder.objects.all()
        serializer = ProductOrderSerializer(p_orders, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ProductOrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

