from rest_framework import viewsets, status
from rest_framework.response import Response
from app.models import User, Product, Order
from app.serializers import UserSerializer, ProductSerializer, OrderSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.using('users').all()
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        response.data['message'] = "User created successfully."
        return response


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.using('products').all()
    serializer_class = ProductSerializer

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        response.data['message'] = "Product created successfully."
        return response


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.using('orders').all()
    serializer_class = OrderSerializer

    def create(self, request, *args, **kwargs):
        data = request.data
        # Custom logic: Ensure user and product exist
        if not User.objects.using('users').filter(id=data.get('user_id')).exists():
            return Response(
                {"error": "User does not exist."},
                status=status.HTTP_400_BAD_REQUEST
            )
        if not Product.objects.using('products').filter(id=data.get('product_id')).exists():
            return Response(
                {"error": "Product does not exist."},
                status=status.HTTP_400_BAD_REQUEST
            )
        response = super().create(request, *args, **kwargs)
        response.data['message'] = "Order created successfully."
        return response
