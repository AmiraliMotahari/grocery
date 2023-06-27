# Generated by Django 4.2 on 2023-06-27 07:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0013_alter_product_ptype'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='cityId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.city', verbose_name='City Name'),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=200),
        ),
    ]
