# Generated by Django 4.2.3 on 2023-07-26 13:16

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("registries", "0003_specialisation_and_more"),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name="kebele",
            unique_together={("name", "woreda")},
        ),
    ]
