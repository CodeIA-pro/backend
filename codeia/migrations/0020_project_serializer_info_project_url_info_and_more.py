# Generated by Django 4.1.11 on 2024-04-26 04:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("codeia", "0019_forgotten"),
    ]

    operations = [
        migrations.AddField(
            model_name="project",
            name="serializer_info",
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name="project",
            name="url_info",
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name="project",
            name="view_info",
            field=models.TextField(blank=True),
        ),
    ]