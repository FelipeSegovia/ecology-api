# Generated by Django 4.2.8 on 2023-12-17 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("ecology", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="ecology",
            name="objetive",
            field=models.BooleanField(default=False, verbose_name="objetives"),
        ),
        migrations.AlterField(
            model_name="ecology",
            name="responsible",
            field=models.BooleanField(default=False, verbose_name="responsible"),
        ),
    ]