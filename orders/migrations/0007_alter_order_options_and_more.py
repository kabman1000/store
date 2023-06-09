# Generated by Django 4.1.6 on 2023-02-15 09:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('store', '0002_product_can_backorder_product_featured_and_more'),
        ('orders', '0006_rename_shipping_address_order_address1_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={'ordering': ('-created',)},
        ),
        migrations.RenameField(
            model_name='order',
            old_name='inventory_updated',
            new_name='billing_status',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='timestamp',
            new_name='created',
        ),
        migrations.RemoveField(
            model_name='order',
            name='paid',
        ),
        migrations.RemoveField(
            model_name='order',
            name='product',
        ),
        migrations.RemoveField(
            model_name='order',
            name='status',
        ),
        migrations.RemoveField(
            model_name='order',
            name='subtotal',
        ),
        migrations.RemoveField(
            model_name='order',
            name='tax',
        ),
        migrations.RemoveField(
            model_name='order',
            name='total',
        ),
        migrations.AddField(
            model_name='order',
            name='total_paid',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5),
        ),
        migrations.AddField(
            model_name='order',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='address1',
            field=models.CharField(default='1234 Main', max_length=250),
        ),
        migrations.AlterField(
            model_name='order',
            name='full_name',
            field=models.CharField(default='Edmund Kabutey', max_length=50),
        ),
        migrations.AlterField(
            model_name='order',
            name='phone',
            field=models.CharField(default='0244546856', max_length=100),
        ),
        migrations.AlterField(
            model_name='order',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='orders.order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_items', to='store.product')),
            ],
        ),
    ]
