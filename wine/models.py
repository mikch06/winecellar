import datetime
from django.db import models
from django.forms import ModelForm
from django.db.models import Sum, Count
from django import template

class Wine(models.Model):
    winename = models.CharField(max_length=200, blank=True,)
    producer = models.CharField(max_length=200, blank=True,)
    grapes = models.CharField(max_length=200, blank=True,)
    year = models.CharField(max_length=200, blank=True,)
    country = models.CharField(max_length=200, blank=True,)
    region = models.CharField(max_length=200, blank=True,)
    purchase = models.DateField(max_length=200, blank=True, null=True,)
    notes = models.CharField(max_length=400, blank=True,)
    drinkfrom = models.CharField(max_length=200, blank=True,)
    drinkto = models.CharField(max_length=200, blank=True,)
    nmbrbottles = models.IntegerField(default=0)
    editdate = models.DateField(auto_now=True,)

    class Meta:
        ordering = ["country","region"]

    # def bottles(self):
    #     result = Wine.objects.aggregate(bottles_sum=Sum('nmbrbottles'))
    #     return result['bottles_sum']