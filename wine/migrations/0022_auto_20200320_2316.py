# Generated by Django 3.0.2 on 2020-03-20 22:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wine', '0021_auto_20200229_1618'),
    ]

    operations = [
        migrations.AddField(
            model_name='wine',
            name='dealer',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='wine',
            name='price',
            field=models.IntegerField(default=0),
        ),
    ]
