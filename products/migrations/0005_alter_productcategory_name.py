# Generated by Django 4.2 on 2023-05-10 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_alter_product_image_alter_product_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productcategory',
            name='name',
            field=models.CharField(max_length=128, unique=True),
        ),
    ]
