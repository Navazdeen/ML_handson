# Generated by Django 4.1 on 2023-01-29 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Home", "0002_studentbio_dob"),
    ]

    operations = [
        migrations.AlterField(
            model_name="studentbio",
            name="DoB",
            field=models.DateField(),
        ),
    ]
