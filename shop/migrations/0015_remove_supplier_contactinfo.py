# Generated by Django 4.2 on 2023-06-27 07:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0014_alter_product_cityid_alter_product_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='supplier',
            name='contactInfo',
        ),
    ]
