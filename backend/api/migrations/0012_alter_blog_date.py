# Generated by Django 4.1 on 2022-08-29 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0011_alter_blog_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="blog",
            name="date",
            field=models.DateTimeField(default="29.08.2022 - 16:29:00"),
        ),
    ]