# Generated by Django 2.0.4 on 2018-08-30 21:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wine', '0006_auto_20180830_2348'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wine',
            name='country',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
