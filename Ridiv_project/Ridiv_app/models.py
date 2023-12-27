from django.db import models

# Create your models here.
class Invoice(models.Model):
    date = models.DateField()
    customer_name = models.CharField(max_length=255)

    def _str_(self):
        return f"Invoice #{self.pk} - {self.customer_name}"

class InvoiceDetail(models.Model):
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE)
    description = models.CharField(max_length=255)
    quantity = models.PositiveIntegerField()
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    price = models.DecimalField(max_digits=10, decimal_places=2, editable=False)

    def save(self, *args, **kwargs):
        # Automatically calculate the total price before saving
        self.price = self.quantity * self.unit_price
        super().save(*args, **kwargs)

    def _str_(self):
        return f"Detail #{self.pk} - {self.description} ({self.quantity} x {self.unit_price})"