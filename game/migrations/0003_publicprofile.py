# Generated by Django 4.2 on 2023-11-25 01:49

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("game", "0002_player_character_creation_state"),
    ]

    operations = [
        migrations.CreateModel(
            name="PublicProfile",
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
                ("name", models.CharField(max_length=100)),
                ("description", models.TextField()),
                ("quality_1", models.CharField(max_length=100)),
                ("quality_2", models.CharField(max_length=100)),
                ("quality_3", models.CharField(max_length=100)),
                ("interest_1", models.CharField(max_length=100)),
                ("interest_2", models.CharField(max_length=100)),
                ("interest_3", models.CharField(max_length=100)),
                ("activity_1", models.CharField(max_length=100)),
                ("activity_2", models.CharField(max_length=100)),
            ],
        ),
    ]
