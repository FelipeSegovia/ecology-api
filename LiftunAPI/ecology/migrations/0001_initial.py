# Generated by Django 4.2.8 on 2023-12-17 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Ecology",
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
                (
                    "fingerPrint",
                    models.BooleanField(default=False, verbose_name="fingerprint"),
                ),
                (
                    "legalObligation",
                    models.BooleanField(default=False, verbose_name="legal_obligation"),
                ),
                (
                    "objetive",
                    models.BooleanField(default=False, verbose_name="Objetives"),
                ),
                (
                    "responsible",
                    models.BooleanField(default=False, verbose_name="Responsible"),
                ),
                (
                    "nameResponsible",
                    models.CharField(max_length=75, verbose_name="name_responsible"),
                ),
            ],
        ),
    ]
