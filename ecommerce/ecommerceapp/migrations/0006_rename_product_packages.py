# Generated by Django 4.1.7 on 2023-08-02 08:48

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("ecommerceapp", "0005_product_package_category"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Product",
            new_name="Packages",
        ),
    ]
