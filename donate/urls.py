from django.urls import path
from .views import CreateReceiptAPIView, ListReceiptAPIView, ListRecentPaymentsAPIView

urlpatterns = [
    path('create',CreateReceiptAPIView.as_view(), name='receipt-create'),
    path('payment-history',ListReceiptAPIView.as_view(), name='receipt-list'),
    path('recent-payments',ListRecentPaymentsAPIView.as_view(), name='recent-receipt-list')
]
