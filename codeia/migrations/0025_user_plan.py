# Generated by Django 4.1.11 on 2024-05-04 02:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("codeia", "0024_plan_subscription"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="plan",
            field=models.IntegerField(default=0),
        ),
    ]