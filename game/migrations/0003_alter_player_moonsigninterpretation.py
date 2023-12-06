# Generated by Django 4.2 on 2023-12-06 00:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("game", "0002_moonsigninterpretation_on_player_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="player",
            name="MoonSignInterpretation",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="game.moonsigninterpretation",
            ),
        ),
    ]
