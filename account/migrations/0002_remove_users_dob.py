# Generated by Django 3.0.1 on 2023-04-15 20:03

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("account", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="users",
            name="dob",
        ),
    ]