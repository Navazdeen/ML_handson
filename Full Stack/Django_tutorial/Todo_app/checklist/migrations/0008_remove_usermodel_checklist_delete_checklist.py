# Generated by Django 4.1 on 2023-02-11 08:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("checklist", "0007_usermodel_phone"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="usermodel",
            name="checklist",
        ),
        migrations.DeleteModel(
            name="CheckList",
        ),
    ]
