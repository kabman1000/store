# Generated by Django 4.1.6 on 2024-04-12 16:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0007_rename_quantity_sold_inventoryreport_amount_sold_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitem',
            name='order',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='items', to='orders.order'),
        ),
    ]
