# Generated by Django 4.1 on 2022-08-22 21:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0003_abyssraids_slug_legionraids_slug"),
    ]

    operations = [
        migrations.AlterField(
            model_name="abyssraids",
            name="image",
            field=models.ImageField(blank=True, null=True, upload_to="abyssraids/"),
        ),
        migrations.AlterField(
            model_name="legionraids",
            name="image",
            field=models.ImageField(blank=True, null=True, upload_to="legionraids/"),
        ),
    ]
