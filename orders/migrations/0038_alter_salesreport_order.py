# Generated by Django 4.1.6 on 2024-06-04 05:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0037_alter_salesreport_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='salesreport',
            name='order',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sales_reports', to='orders.order'),
        ),
    ]
