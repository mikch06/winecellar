# Generated by Django 3.0.2 on 2020-01-19 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wine', '0010_auto_20200119_1833'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wine',
            name='nmbrbottles',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]
