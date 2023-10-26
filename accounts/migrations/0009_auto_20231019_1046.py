# Generated by Django 4.2 on 2023-10-19 14:46

from django.db import migrations


def update_gender_codes(apps, schema_editor):
    DatingPreference = apps.get_model("accounts", "DatingPreference")

    mapping = {"Males": "M", "Females": "F", "Non-binary Individuals": "N"}

    for pref in DatingPreference.objects.all():
        if pref.gender in mapping:
            pref.gender = mapping[pref.gender]
            pref.save()


class Migration(migrations.Migration):
    dependencies = [
        ("accounts", "0008_alter_datingpreference_gender_alter_profile_gender"),
    ]

    operations = [
        migrations.RunPython(
            update_gender_codes, reverse_code=migrations.RunPython.noop
        )
    ]
