# Generated by Django 4.2 on 2023-07-01 13:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0025_swiper'),
    ]

    operations = [
        migrations.RenameField(
            model_name='swiper',
            old_name='h',
            new_name='header',
        ),
        migrations.RenameField(
            model_name='swiper',
            old_name='p',
            new_name='pragraph',
        ),
    ]
