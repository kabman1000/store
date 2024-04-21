from django.contrib import admin

from .models import Order, OrderItem, InventoryReport

admin.site.register(Order)
admin.site.register(OrderItem)

@admin.register(InventoryReport)
class InventoryAdmin(admin.ModelAdmin):
    list_display = ['product', 'days_on_hand','inventory_on_hand','amount_sold']