# Generated by Django 4.2.6 on 2024-03-18 22:08

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("schedule", "0008_rename_uid_instructor_ins_id_and_more"),
    ]

    operations = [
        migrations.DeleteModel(
            name="Schedule",
        ),
    ]
