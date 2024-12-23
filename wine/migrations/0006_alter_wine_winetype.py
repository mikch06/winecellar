# Generated by Django 5.0.10 on 2024-12-23 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("wine", "0005_alter_wine_options_wine_winetype"),
    ]

    operations = [
        migrations.AlterField(
            model_name="wine",
            name="winetype",
            field=models.CharField(
                blank=True,
                choices=[
                    ("-", "-"),
                    ("red", "Rot"),
                    ("white", "Weiss"),
                    ("rose", "Rosé"),
                    ("bubbles", "Bubbles"),
                    ("sweet", "Süsswein"),
                    ("spirit", "Spirituosen"),
                ],
                default="-",
                max_length=12,
            ),
        ),
    ]
