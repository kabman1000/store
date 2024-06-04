# Generated by Django 4.1.6 on 2024-05-30 12:23

from decimal import Decimal
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0009_alter_product_title'),
        ('orders', '0021_order_balance'),
    ]

    operations = [
        migrations.CreateModel(
            name='SalesReport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('report_start_date', models.DateField()),
                ('report_end_date', models.DateField()),
                ('total_sales', models.DecimalField(decimal_places=2, default=Decimal('0.00'), max_digits=10)),
                ('total_units_sold', models.PositiveIntegerField(default=0)),
                ('number_of_transactions', models.PositiveIntegerField(default=0)),
                ('average_transaction_value', models.DecimalField(decimal_places=2, default=Decimal('0.00'), max_digits=10)),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('product', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='store.product')),
            ],
        ),
    ]