import datetime
from django.db import models
from django.forms import ModelForm
from django.db.models import Sum, Count

class Wine(models.Model):
    winename = models.CharField(max_length=200, blank=True,)
    producer = models.CharField(max_length=200, blank=True,)
    grapes = models.CharField(max_length=200, blank=True,)
    year = models.CharField(max_length=200, blank=True,)
    country = models.CharField(max_length=200, blank=True,)
    region = models.CharField(max_length=200, blank=True,)
    purchase = models.CharField(max_length=200, blank=True,)
    notes = models.CharField(max_length=400, blank=True,)
    drinkfrom = models.CharField(max_length=200, blank=True,)
    drinkto = models.CharField(max_length=200, blank=True,)
    nmbrbottles = models.IntegerField(default=0)
    editdate = models.DateField(auto_now=True,)
    
    class Meta:
        ordering = ["country","region"]

    def bottles(self):
        #return self.choice_set.aggregate(Sum('votes'))['votes__sum']
        #return Wine.objects.aggregate(Sum('nmbrbottles'))['nmbrbottles__sum']
        return Wine.objects.aggregate(bottles=Sum('nmbrbottles'))
