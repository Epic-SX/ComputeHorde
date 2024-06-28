# Generated by Django 4.2.13 on 2024-06-27 11:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("validator", "0018_alter_systemevent_subtype_alter_systemevent_type"),
    ]

    operations = [
        migrations.CreateModel(
            name="MinerManifest",
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
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("executor_count", models.IntegerField(default=0)),
                (
                    "batch",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="validator.syntheticjobbatch",
                    ),
                ),
                (
                    "miner",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="validator.miner",
                    ),
                ),
            ],
        ),
        migrations.AddConstraint(
            model_name="minermanifest",
            constraint=models.UniqueConstraint(
                fields=("miner", "batch"), name="unique_miner_manifest"
            ),
        ),
    ]
