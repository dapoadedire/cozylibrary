# Generated by Django 4.1 on 2022-10-14 06:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("cozylibrary", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="book",
            name="created_at",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2022, 10, 14, 6, 39, 59, 953614, tzinfo=datetime.timezone.utc
                ),
                editable=False,
            ),
        ),
    ]
