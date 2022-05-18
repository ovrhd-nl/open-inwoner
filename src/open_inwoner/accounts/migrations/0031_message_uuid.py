# Generated by Django 3.2.12 on 2022-03-14 10:54

import uuid

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0030_message_file"),
    ]

    operations = [
        migrations.AddField(
            model_name="message",
            name="uuid",
            field=models.UUIDField(
                default=uuid.uuid4, help_text="Unique identifier", verbose_name="UUID"
            ),
        ),
    ]
