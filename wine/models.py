import datetime
from django.db import models
from django import forms

class Wine(models.Model):
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

    winename = models.CharField(max_length=200, blank=True)
    producer = models.CharField(max_length=200, blank=True)
    grapes = models.CharField(max_length=200, blank=True,)
    year = models.CharField(max_length=200, blank=True)
    country = models.CharField(max_length=12, choices=COUNTRY)
    region = models.CharField(max_length=200, blank=True)
    purchase = models.DateField(null=True)
    price = models.CharField(max_length=12, blank=True, default=0)
    dealer = models.CharField(max_length=200, blank=True)
    drinkfrom = models.CharField(max_length=200, blank=True)
    drinkto = models.CharField(max_length=200, blank=True)
    nmbrbottles = models.IntegerField(default=0)
    notes = models.CharField(max_length=400, blank=True)
    editdate = models.DateField(auto_now=True)

    class Meta:
        ordering = ["country", "region", "year"]