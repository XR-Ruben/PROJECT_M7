# Generated by Django 5.1 on 2024-09-08 20:07

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("m7_python", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Contact",
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
                ("nombre", models.CharField(max_length=100)),
                ("email", models.CharField(max_length=100)),
                ("mensaje", models.CharField(max_length=500)),
            ],
        ),
    ]
