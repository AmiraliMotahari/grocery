# Generated by Django 4.2.1 on 2023-06-04 14:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0007_alter_inventoryproduct_quantity_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='inventory',
            old_name='city',
            new_name='cityId',
        ),
    ]