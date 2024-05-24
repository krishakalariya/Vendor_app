# vendors/urls.py

from django.urls import path
from .views import VendorListCreateAPIView, VendorRetrieveUpdateDestroyAPIView, \
    PurchaseOrderListCreateAPIView, \
    PurchaseOrderRetrieveUpdateDestroyAPIView, VendorPerformanceAPIView, acknowledge_purchase_order
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('vendors/', VendorListCreateAPIView.as_view(), name='vendor-list-create'),
    path('vendors/<int:pk>/', VendorRetrieveUpdateDestroyAPIView.as_view(), name='vendor-retrieve-update-destroy'),
    path('purchase_orders/', PurchaseOrderListCreateAPIView.as_view(), name='purchase-order-list-create'),
    path('purchase_orders/<int:pk>/', PurchaseOrderRetrieveUpdateDestroyAPIView.as_view(),
         name='purchase-order-retrieve-update-destroy'),
    path('vendors/<int:vendor_id>/performance', VendorPerformanceAPIView.as_view(), name="vendor-performance"),
    path('purchase_orders/<int:pk>/acknowledge/', acknowledge_purchase_order, name='acknowledge-purchase-order'),
]
