# Generated by Django 4.2 on 2023-05-13 10:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_basket'),
    ]

    operations = [
        migrations.RenameField(
            model_name='basket',
            old_name='products',
            new_name='product',
        ),
    ]