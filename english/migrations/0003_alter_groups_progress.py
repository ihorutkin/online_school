# Generated by Django 5.1.1 on 2024-09-19 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("english", "0002_groups_progress"),
    ]

    operations = [
        migrations.AlterField(
            model_name="groups",
            name="progress",
            field=models.DecimalField(decimal_places=8, max_digits=15),
        ),
    ]
