# Generated by Django 3.2 on 2022-08-09 23:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_product_has_key_size'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='has_key_size',
            new_name='keyboard_size',
        ),
    ]
