# Generated by Django 3.2 on 2022-08-10 01:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_alter_product_keyboard_size'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='keyboard_size',
            new_name='has_keys',
        ),
    ]
