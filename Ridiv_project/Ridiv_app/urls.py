
from django.urls import path
from .views import InvoiceView, InvoiceDetailsview
from rest_framework.routers import DefaultRouter

router = DefaultRouter(trailing_slash=False)
router.register('invoice',InvoiceView,basename='invoice')
router.register('invoice-details',InvoiceDetailsview,basename='InvoiceDetail')

urlpatterns = [
    
]+router.urls
