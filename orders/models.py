from decimal import Decimal
from django.conf import settings
from django.db import models
from django.utils import timezone
from store.models import Product


class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='order_user')
    full_name = models.CharField(max_length=50)
    address1 = models.CharField(max_length=250)
    phone = models.CharField(max_length=100)
    created = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(auto_now=True)
    total_paid = models.DecimalField(max_digits=10, decimal_places=2)
    billing_status = models.BooleanField(default=False)
    order_number = models.AutoField(primary_key=True)

    class Meta:
        ordering = ('-created',)
    
    def __str__(self):
        return str(self.created)

        

class OrderItem(models.Model):
    order = models.ForeignKey(Order,
                              related_name='items',
                              on_delete=models.SET_NULL,
                              null= True)
    product = models.ForeignKey(Product,
                                related_name='order_items',
                                on_delete=models.SET_NULL,
                                null= True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return str(self.id)
    
    @property
    def total_cost(self):
        return self.quantity * self.price