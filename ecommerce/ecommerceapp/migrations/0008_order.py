# Generated by Django 4.1.7 on 2023-08-02 15:02

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("ecommerceapp", "0007_rename_packages_package"),
    ]

    operations = [
        migrations.CreateModel(
            name="Order",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=50)),
                ("email", models.EmailField(max_length=254)),
                ("package", models.CharField(max_length=50)),
                ("address", models.TextField(max_length=500)),
                ("payment", models.CharField(max_length=50)),
            ],
        ),
    ]
