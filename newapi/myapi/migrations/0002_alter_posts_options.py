# Generated by Django 4.2 on 2023-04-13 10:52

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("myapi", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="posts",
            options={"verbose_name_plural": "Posts"},
        ),
    ]
