# Generated by Django 2.0.4 on 2018-08-31 05:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wine', '0007_auto_20180830_2350'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='author',
            name='created_by',
        ),
        migrations.AlterField(
            model_name='wine',
            name='drinkfrom',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='wine',
            name='drinkto',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='wine',
            name='grapes',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='wine',
            name='nmbrbottles',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='wine',
            name='year',
            field=models.CharField(max_length=200),
        ),
        migrations.DeleteModel(
            name='Author',
        ),
    ]
