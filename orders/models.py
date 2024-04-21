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
                              on_delete=models.CASCADE,
                              null= True)
    product = models.ForeignKey(Product,
                                related_name='order_items',
                                on_delete=models.SET_NULL,
                                null= True,
                                to_field='title')
    price = models.DecimalField(max_digits=6, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)
    inventory = models.PositiveIntegerField(default=0)

    def __str__(self):
        return str(self.id)
    
    @property
    def total_cost(self):
        return self.quantity * self.price




class InventoryReport(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE)
    days_on_hand = models.PositiveIntegerField(default=0)
    inventory_on_hand = models.PositiveIntegerField(default=0)
    amount_sold = models.PositiveIntegerField(default=0)

    def calculate_days_on_hand(self):
    # Calculate days on hand based on last order date
        if self.product.created:
            days_on_hand = (timezone.now() - self.product.created).days
            return days_on_hand
        return 0

    def calculate_inventory_on_hand(self):
        # Calculate inventory on hand
        return self.product.inventory

    def calculate_amount_sold(self):
        # Calculate total amount sold
        total_amount_sold = self.product.order_items.aggregate(total=models.Sum('quantity'))['total']
        return total_amount_sold if total_amount_sold else 0

    def save(self, *args, **kwargs):
        self.days_on_hand = self.calculate_days_on_hand()
        self.inventory_on_hand = self.calculate_inventory_on_hand()
        self.amount_sold = self.calculate_amount_sold()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Inventory Report for {self.product.title}"