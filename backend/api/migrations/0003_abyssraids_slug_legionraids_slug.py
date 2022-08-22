# Generated by Django 4.1 on 2022-08-22 21:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0002_alter_abyssraids_image_alter_legionraids_image"),
    ]

    operations = [
        migrations.AddField(
            model_name="abyssraids",
            name="slug",
            field=models.SlugField(null=True, unique=True),
        ),
        migrations.AddField(
            model_name="legionraids",
            name="slug",
            field=models.SlugField(null=True, unique=True),
        ),
    ]
