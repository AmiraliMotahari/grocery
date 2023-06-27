# Generated by Django 4.2 on 2023-06-27 09:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0018_remove_supplier_name_supplier_lastname_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventoryproduct',
            name='inventoryId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.inventory', verbose_name='Inventory City'),
        ),
        migrations.AlterField(
            model_name='inventoryproduct',
            name='productId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.product', verbose_name='Product Name'),
        ),
    ]