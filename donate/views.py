from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Receipt
from .serializers import ReceiptSerializer


class CreateReceiptAPIView(generics.CreateAPIView):
    queryset = Receipt.objects.all()
    serializer_class = ReceiptSerializer

class ListReceiptAPIView(generics.ListAPIView):
    queryset = Receipt.objects.all()
    serializer_class = ReceiptSerializer

class ListRecentPaymentsAPIView(APIView):
    def get(self, request):
        recent_payments = Receipt.objects.all().order_by('-id')[:5]
        serializer = ReceiptSerializer(recent_payments, many=True)
        return Response(serializer.data)