import datetime
from django.db import models
from django.db.models import Count


class Wine(models.Model):
    winename = models.CharField(max_length=200, blank=True,)
    producer = models.CharField(max_length=200, blank=True,)
    grapes = models.CharField(max_length=200, blank=True,)
    year = models.CharField(max_length=200, blank=True,)
    country = models.CharField(max_length=200, blank=True,)
    region = models.CharField(max_length=200, blank=True,)
    purchase = models.DateField(max_length=200, blank=True, null=True,)
    price = models.IntegerField(default="",)
    dealer = models.CharField(max_length=200, blank=True,)
    drinkfrom = models.CharField(max_length=200, blank=True,)
    drinkto = models.CharField(max_length=200, blank=True,)
    nmbrbottles = models.IntegerField(default=0)
    notes = models.CharField(max_length=400, blank=True,)
    editdate = models.DateField(auto_now=True,)

    class Meta:
        ordering = ["country", "region", "year"]