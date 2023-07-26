# Generated by Django 4.2.3 on 2023-07-26 00:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="EducationLevel",
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
        migrations.CreateModel(
            name="Gender",
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
        migrations.CreateModel(
            name="MaritalStatus",
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
        migrations.CreateModel(
            name="Position",
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
        migrations.CreateModel(
            name="Region",
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
        migrations.CreateModel(
            name="Salutation",
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
        migrations.CreateModel(
            name="Zone",
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
                (
                    "region",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="zones",
                        to="registries.region",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Woreda",
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
                (
                    "zone",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="woredas",
                        to="registries.zone",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Kebele",
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
                (
                    "woreda",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="kebeles",
                        to="registries.woreda",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="DevelopmentGroup",
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
                (
                    "kebele",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="development_groups",
                        to="registries.kebele",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="DevelopmentAgent",
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
                ("name", models.TextField()),
                ("father_name", models.TextField()),
                ("grand_father_name", models.TextField()),
                ("birth_month", models.IntegerField()),
                ("birth_year", models.IntegerField()),
                ("phone_number", models.TextField()),
                ("alternate_phone_number", models.TextField()),
                ("email", models.TextField()),
                ("specialization", models.TextField(null=True)),
                ("specialization_other", models.TextField(null=True)),
                ("employment_month", models.IntegerField()),
                ("employment_year", models.IntegerField()),
                ("assignment_month", models.IntegerField()),
                ("assignment_year", models.IntegerField()),
                ("pension_number", models.TextField()),
                (
                    "development_group",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="registries.developmentgroup",
                    ),
                ),
                (
                    "education_level",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="registries.educationlevel",
                    ),
                ),
                (
                    "gender",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="registries.gender",
                    ),
                ),
                (
                    "kebele",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="registries.kebele",
                    ),
                ),
                (
                    "marital_status",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="registries.maritalstatus",
                    ),
                ),
                (
                    "position",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="registries.position",
                    ),
                ),
                (
                    "region",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="registries.region",
                    ),
                ),
                (
                    "salutation",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="registries.salutation",
                    ),
                ),
                (
                    "woreda",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="registries.woreda",
                    ),
                ),
                (
                    "zone",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="registries.zone",
                    ),
                ),
            ],
            options={
                "db_table": "DAAS_Registries",
            },
        ),
    ]