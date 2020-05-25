# Generated by Django 3.0.6 on 2020-05-23 19:04

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="DuckType",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="FoodType",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="Record",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "recorddate",
                    models.DateTimeField(
                        default=datetime.datetime(
                            2020, 5, 23, 19, 4, 11, 533456, tzinfo=utc
                        )
                    ),
                ),
                ("location", models.CharField(max_length=100)),
                ("howmany_ducks", models.PositiveIntegerField()),
                ("howmuch_food", models.CharField(max_length=100)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "duck_type",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="ducks.DuckType"
                    ),
                ),
                (
                    "food_type",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="ducks.FoodType"
                    ),
                ),
            ],
        ),
    ]
