from django.contrib import admin
import csv
from django.http import HttpResponse
from .models import Order, OrderItem, InventoryReport, SalesReport
from rangefilter.filters import DateRangeFilter, DateTimeRangeFilter

admin.site.register(Order)
admin.site.register(OrderItem)

@admin.register(InventoryReport)
class InventoryAdmin(admin.ModelAdmin):
    actions = ["export_as_csv"]

    def export_as_csv(self, request, queryset):
        meta = self.model._meta
<<<<<<< HEAD
        field_names = [field.name for field in meta.fields if field.name not in ["id"]]
=======
        field_names = [field.name for field in meta.fields if field.name not in ["created","id"]]
>>>>>>> f0b1e47d8f1b0f93635e3c366d69759cec10ce6b

        earliest_date = queryset.order_by('created').values_list('created', flat=True).first()
        latest_date = queryset.order_by('-created').values_list('created', flat=True).first()

        if earliest_date and latest_date:
            formatted_earliest_date = earliest_date.strftime('%Y-%m-%d')
            formatted_latest_date = latest_date.strftime('%Y-%m-%d')
            date_range = f"{formatted_earliest_date} to {formatted_latest_date}"
            formatted_date = formatted_latest_date  # Use the latest date for the filename
        else:
            # Fallback to the current date if no date is found
            formatted_date = datetime.now().strftime('%Y-%m-%d')
            date_range = f"Date: {formatted_date}"

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = f'attachment; filename=inventory_{formatted_date}.csv'

<<<<<<< HEAD
        writer = csv.writer(response)
        
=======
>>>>>>> f0b1e47d8f1b0f93635e3c366d69759cec10ce6b
        # Write the date range at the top of the CSV file
        writer.writerow([f"Inventory Report for: {date_range}"])
        writer.writerow([])  # Add an empty row for spacing
        writer.writerow(field_names)  # Write the header row

        for obj in queryset:
            row = [getattr(obj, field) for field in field_names]
            writer.writerow(row)

        return response

    export_as_csv.short_description = "Export Selected"
<<<<<<< HEAD

    list_filter = (('created', DateRangeFilter),('created', DateRangeFilter))
=======
    list_filter = (('created', DateRangeFilter), ('created', DateTimeRangeFilter))
>>>>>>> f0b1e47d8f1b0f93635e3c366d69759cec10ce6b
    list_display = ['product', 'days_on_hand','inventory_on_hand','quantity_sold','created']



@admin.register(SalesReport)
class SalesAdmin(admin.ModelAdmin):
    actions = ["export_as_csv"]

    def export_as_csv(self, request, queryset):
        meta = self.model._meta
<<<<<<< HEAD
        field_names = [field.name for field in meta.fields if field.name not in [ "order","id"]]
=======
        field_names = [field.name for field in meta.fields if field.name not in ["date_created", "order","id"]]
>>>>>>> f0b1e47d8f1b0f93635e3c366d69759cec10ce6b

        earliest_date = queryset.order_by('date_created').values_list('date_created', flat=True).first()
        latest_date = queryset.order_by('-date_created').values_list('date_created', flat=True).first()

        if earliest_date and latest_date:
            formatted_earliest_date = earliest_date.strftime('%Y-%m-%d')
            formatted_latest_date = latest_date.strftime('%Y-%m-%d')
            date_range = f"{formatted_earliest_date} to {formatted_latest_date}"
            formatted_date = formatted_latest_date  # Use the latest date for the filename
        else:
            # Fallback to the current date if no date is found
            formatted_date = datetime.now().strftime('%Y-%m-%d')
            date_range = f"Date: {formatted_date}"

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = f'attachment; filename=sales_{formatted_date}.csv'
        
        writer = csv.writer(response)

        # Write the date range at the top of the CSV file
        writer.writerow([f"Sales Report for: {date_range}"])
        writer.writerow([])  # Add an empty row for spacing
        writer.writerow(field_names)  # Write the header row

        for obj in queryset:
            row = [getattr(obj, field) for field in field_names]
            writer.writerow(row)

        return response

    export_as_csv.short_description = "Export Selected"
    list_filter = (('date_created', DateRangeFilter), ('date_created', DateTimeRangeFilter))
    list_display = ['product','total_sales','total_units_sold','number_of_transactions','average_transaction_value','date_created']