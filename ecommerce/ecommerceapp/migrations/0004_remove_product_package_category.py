# Generated by Django 4.1.7 on 2023-08-02 08:29

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("ecommerceapp", "0003_rename_category_product_package_category_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="product",
            name="package_category",
        ),
    ]