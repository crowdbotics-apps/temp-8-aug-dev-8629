# Generated by Django 2.2.15 on 2020-08-08 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="name",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
