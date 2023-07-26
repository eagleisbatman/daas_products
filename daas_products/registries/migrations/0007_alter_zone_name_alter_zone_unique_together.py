# Generated by Django 4.2.3 on 2023-07-26 13:41

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("registries", "0006_alter_woreda_name_alter_woreda_unique_together"),
    ]

    operations = [
        migrations.AlterField(
            model_name="zone",
            name="name",
            field=models.CharField(max_length=255),
        ),
        migrations.AlterUniqueTogether(
            name="zone",
            unique_together={("name", "region")},
        ),
    ]