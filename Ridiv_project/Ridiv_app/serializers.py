from rest_framework import serializers
from .models import Invoice, InvoiceDetail


class InvoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model=Invoice
        fields = '__all__'

class InvoiceDetailSerializer(serializers.ModelSerializer):
    invoice = InvoiceSerializer(read_only = True)
    invoice_id = serializers.IntegerField(write_only=True)
    class Meta:
        model = InvoiceDetail
        fields = ['id','description','quantity','unit_price','price','invoice','invoice_id']