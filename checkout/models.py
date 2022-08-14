import uuid

from django.db import models
from django.db.models import Sum
from django.conf import settings

from products.models import Product


class Checkout(models.Model):
    full_name = models.CharField(max_length=50, blank=False, null=False,)
    phone_number = models.CharField(max_length=20, blank=False, null=False)
    email_address = models.EmailField(max_length=150, blank=False, null=False)
    city = models.CharField(max_length=40, blank=False, null=False)
    country = models.CharField(max_length=50, blank=False, null=False)
    street_address_1 = models.CharField(max_length=80, blank=False, null=False)
    street_address_2 = models.CharField(max_length=80, blank=True, null=True)
    county = models.CharField(max_length=80, blank=True, null=True)
    postal_address = models.CharField(max_length=20, blank=False, null=True)
    order_id = models.CharField(max_length=32, null=False, editable=False)
    checkout_date = models.DateTimeField(auto_now_add=True)
    delivery_cost = models.DecimalField(max_digits=6, decimal_places=2, default=0, null=False)
    order_total_cost = models.DecimalField(max_digits=10, decimal_places=2, default=0, null=False)
    grand_total = models.DecimalField(max_digits=10, decimal_places=2, default=0, null=False)

    def _generate_order_id(self):
        """
        Generates a unique, random order number each order
        """
        return uuid.uuid4().hex.upper()

    def update_total(self):
        """
        Update grand total each time a line item is added,
        accounting for delivery costs.
        """
        self.grand_total = self.lineitems.aggregate(
            Sum('order_total_cost'))['lineitem_total'] or 0
        self.save()


    def save(self, *args, **kwargs):
        """
        Overwrites the original save method for setting an order 
        number if it hasn't been set already.
        """
        if not self.order_id:
            self.order_id = self._generate_order_id()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.order_id


class LineItems(models.Model):
    checkout = models.ForeignKey(Checkout, blank=False, null=False, on_delete=models.CASCADE, related_name='lineitems')
    product = models.ForeignKey(Product, blank=False, null=False, on_delete=models.CASCADE)
    quantity = models.IntegerField(blank=False, null=False, default=0)
    number_of_keys = models.CharField(max_length=3, blank=True, null=True)
    lineitem_total = models.DecimalField(max_digits=6, decimal_places=2, blank=False, null=False, editable=False)

    def save(self, *args, **kwargs):
        """
        Overwrites the original save method for setting the line item 
        total and updates the order total accordingly.
        """
        self.lineitem_total = self.product.price * self.quantity
        super().save(*args, **kwargs)

    def __str__(self):
        return f'SKU {self.product.sku} on order {self.checkout.order_id}'