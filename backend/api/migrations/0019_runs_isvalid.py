# Generated by Django 4.1 on 2022-09-09 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0018_alter_blog_date"),
    ]

    operations = [
        migrations.AddField(
            model_name="runs",
            name="isValid",
            field=models.BooleanField(default=False),
        ),
    ]