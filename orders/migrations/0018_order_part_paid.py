# Generated by Django 4.1.6 on 2024-05-29 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0017_remove_inventoryreport_last_inventory_change'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='part_paid',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]
