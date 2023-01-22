# Generated by Django 4.1 on 2023-01-22 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="StudentBio",
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
                ("Email", models.EmailField(max_length=254)),
                ("Name", models.CharField(max_length=255)),
                ("Age", models.IntegerField()),
                ("Gender", models.CharField(max_length=1)),
            ],
        ),
    ]
