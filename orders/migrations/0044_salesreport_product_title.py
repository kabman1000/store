# Generated by Django 4.1.6 on 2024-06-08 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0043_salesreport_product_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='salesreport',
            name='product_title',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
