# Generated by Django 4.1.6 on 2024-04-09 04:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_product_total_value'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='total_value',
            field=models.DecimalField(decimal_places=2, max_digits=10, max_length=255),
        ),
    ]
