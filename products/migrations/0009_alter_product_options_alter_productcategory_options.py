# Generated by Django 4.2 on 2023-05-13 20:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_rename_products_basket_product'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name_plural': 'Products'},
        ),
        migrations.AlterModelOptions(
            name='productcategory',
            options={'verbose_name_plural': 'Categories'},
        ),
    ]
