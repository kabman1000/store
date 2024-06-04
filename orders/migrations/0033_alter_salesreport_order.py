# Generated by Django 4.1.6 on 2024-06-04 05:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0032_remove_salesreport_order_salesreport_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='salesreport',
            name='order',
            field=models.ManyToManyField(related_name='sales_reports', to='orders.order'),
        ),
    ]
