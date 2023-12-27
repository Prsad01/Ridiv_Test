from django.urls import reverse
from .serializers import InvoiceDetailSerializer
from .models import InvoiceDetail,Invoice

from rest_framework.test import APITestCase, APIClient
from rest_framework import status

class Get_All_Invoces_Test(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.inv = Invoice.objects.create(customer_name='prasad',date='2023-12-27')
        self.invoice = InvoiceDetail.objects.create(invoice=self.inv,description="temp",quantity=2,unit_price=10)

    def test_get_all_invoices(self):
        url = reverse('InvoiceDetail-list')
        response= self.client.get(url)

        expected_data = InvoiceDetail.objects.all()
        expected_data = InvoiceDetailSerializer(expected_data,many=True)

        self.assertEqual(response.status_code,status.HTTP_200_OK)
        self.assertEqual(response.data,expected_data.data)
    
    def test_get_single_invoice(self):
        url = reverse('InvoiceDetail-detail', kwargs={'pk': self.invoice.pk})
        response = self.client.get(url)

        expected_data = InvoiceDetailSerializer(instance=self.invoice)

        self.assertEqual(response.status_code,status.HTTP_200_OK)
        self.assertEqual(response.data,expected_data.data)

    def test_post_invoice(self):
        url = reverse('InvoiceDetail-list')
        payload = {"invoice_id":self.inv.pk, "description":"temp","quantity":"2","unit_price":"10"}
        response = self.client.post(path=url,data=payload,format='json')
        self.assertEqual(response.status_code,status.HTTP_201_CREATED)
