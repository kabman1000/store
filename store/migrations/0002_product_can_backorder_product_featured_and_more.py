# Generated by Django 4.1.6 on 2023-02-14 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='can_backorder',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='product',
            name='featured',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='product',
            name='inventory',
            field=models.IntegerField(default=0),
        ),
    ]
