# Generated by Django 4.0.1 on 2022-12-03 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wine', '0003_remove_wine_storage'),
    ]

    operations = [
        migrations.AddField(
            model_name='wine',
            name='warehouse',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
