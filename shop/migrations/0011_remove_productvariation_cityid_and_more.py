# Generated by Django 4.2 on 2023-06-27 07:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0010_delete_category_remove_productvariation_pvtype_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productvariation',
            name='cityId',
        ),
        migrations.RemoveField(
            model_name='productvariation',
            name='price',
        ),
        migrations.RemoveField(
            model_name='productvariation',
            name='productId',
        ),
        migrations.RemoveField(
            model_name='productvariation',
            name='quantity',
        ),
        migrations.AlterField(
            model_name='product',
            name='pType',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.productvariation'),
        ),
        migrations.AlterField(
            model_name='productvariation',
            name='name',
            field=models.CharField(max_length=200, verbose_name='Category Name'),
        ),
    ]
