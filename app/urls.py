from django.urls import path, include
from rest_framework.routers import DefaultRouter
from app.views import UserViewSet, ProductViewSet, OrderViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')
router.register(r'products', ProductViewSet, basename='product')
router.register(r'orders', OrderViewSet, basename='order')

urlpatterns = [
    path('api/', include(router.urls)),
]
