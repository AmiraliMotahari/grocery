# Generated by Django 4.2 on 2023-06-27 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0011_remove_productvariation_cityid_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='pType',
            field=models.CharField(max_length=200, verbose_name='Product Type'),
        ),
    ]
