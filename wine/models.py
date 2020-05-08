import datetime
from django.db import models
from django import forms
from django.forms import ModelForm

COUNTRY = [
    ('x', 'x'),
    ('Australien', 'Australien'),
    ('Frankreich', 'Frankreich'),
    ('Deutschland', 'Deutschland'),
    ('Italien', 'Italien'),
    ('Österreich', 'Österreich'),
    ('Portugal', 'Portugal'),
    ('Schweiz', 'Schweiz'),
    ('Spanien', 'Spanien'),
    ('Südafrika', 'Südafrika'),
    ('USA', 'USA'),
]
class Wine(models.Model):


    winename = models.CharField(max_length=200, blank=True)
    producer = models.CharField(max_length=200, blank=True)
    grapes = models.CharField(max_length=200, blank=True,)
    year = models.CharField(max_length=200, blank=True)
    country = models.CharField(max_length=12, choices=COUNTRY)
    region = models.CharField(max_length=200, blank=True)
    purchase = models.DateField(blank=True, null=True)
    price = models.FloatField(blank=True, default=0)
    dealer = models.CharField(max_length=200, blank=True)
    drinkfrom = models.CharField(max_length=200, blank=True)
    drinkto = models.CharField(max_length=200, blank=True)
    nmbrbottles = models.IntegerField(default=0)
    notes = models.CharField(max_length=400, blank=True)
    editdate = models.DateField(auto_now=True)

    class Meta:
        ordering = ["country", "region", "year"]

class WineForm(ModelForm):
    class Meta:
        model = Wine
        fields = ['winename', 'producer', 'country', 'purchase']
        widgets = {
            'purchase': forms.SelectDateWidget()
        }