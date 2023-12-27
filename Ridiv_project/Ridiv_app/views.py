from django.shortcuts import render
from .models import Invoice, InvoiceDetail
from .serializers import InvoiceSerializer, InvoiceDetailSerializer
from rest_framework import viewsets

# Create your views here.

class InvoiceView(viewsets.ModelViewSet):
    serializer_class = InvoiceSerializer
    queryset = Invoice.objects.all()

class InvoiceDetailsview(viewsets.ModelViewSet):
    serializer_class = InvoiceDetailSerializer
    queryset = InvoiceDetail.objects.select_related().all()
