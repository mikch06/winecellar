import datetime
from django.db import models
from django.forms import ModelForm
from django.db.models import Sum

class Wine(models.Model):
    winename = models.CharField(max_length=200)
    producer = models.CharField(max_length=200)
    grapes = models.CharField(max_length=200)
    year = models.CharField(max_length=200)
    country = models.CharField(max_length=200, null=True,)
    region = models.CharField(max_length=200, null=True,)
    purchase = models.CharField(max_length=200, null=True,)
    notes = models.CharField(max_length=400, null=True,)
    drinkfrom = models.CharField(max_length=200)
    drinkto = models.CharField(max_length=200)
    nmbrbottles = models.IntegerField()
    entrydate = models.DateTimeField('date published', null=True,)
    editdate = models.DateTimeField(null=True,)


    #todo: try to insert sum of nmbrbottles
    #bottles = nmbrbottles.objects.aggregate(Sum('nmbrbottles'))


class NewWineForm(ModelForm):
    class Meta:
        model = Wine
        fields = ['winename', 'producer']

form = NewWineForm()