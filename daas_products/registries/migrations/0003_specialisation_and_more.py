# Generated by Django 4.2.3 on 2023-07-26 12:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("registries", "0002_alter_developmentagent_table"),
    ]

    operations = [
        migrations.CreateModel(
            name="Specialisation",
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
                ("name", models.CharField(max_length=255, unique=True)),
            ],
        ),
        migrations.RemoveField(
            model_name="developmentagent",
            name="development_group",
        ),
        migrations.AlterField(
            model_name="developmentagent",
            name="education_level",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="development_agents",
                to="registries.educationlevel",
            ),
        ),
        migrations.AlterField(
            model_name="developmentagent",
            name="gender",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="development_agents",
                to="registries.gender",
            ),
        ),
        migrations.AlterField(
            model_name="developmentagent",
            name="kebele",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="development_agents",
                to="registries.kebele",
            ),
        ),
        migrations.AlterField(
            model_name="developmentagent",
            name="marital_status",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="development_agents",
                to="registries.maritalstatus",
            ),
        ),
        migrations.AlterField(
            model_name="developmentagent",
            name="position",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="development_agents",
                to="registries.position",
            ),
        ),
        migrations.AlterField(
            model_name="developmentagent",
            name="region",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="development_agents",
                to="registries.region",
            ),
        ),
        migrations.AlterField(
            model_name="developmentagent",
            name="salutation",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="development_agents",
                to="registries.salutation",
            ),
        ),
        migrations.AlterField(
            model_name="developmentagent",
            name="woreda",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="development_agents",
                to="registries.woreda",
            ),
        ),
        migrations.AlterField(
            model_name="developmentagent",
            name="zone",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="development_agents",
                to="registries.zone",
            ),
        ),
        migrations.DeleteModel(
            name="DevelopmentGroup",
        ),
    ]
