from django.db import models
from django.urls import reverse
from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User

COUNTRY = [
    ('-', '-'),
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

WINETYPE = {
    "-": "-",
    "red": "Rot",
    "white": "Weiss",
    "rose": "Rosé",
    "bubbles": "Bubbles",
    "sweet": "Süsswein",
    "spirit": "Spirituosen",
}

class Wine(models.Model):
    owner = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    winename = models.CharField(max_length=200)
    producer = models.CharField(max_length=200, blank=True)
    grapes = models.CharField(max_length=200, blank=True,)
    winetype = models.CharField(max_length=12, blank=True, choices=WINETYPE, default='-')
    year = models.IntegerField(blank=True, null=True)
    country = models.CharField(max_length=12, blank=True, choices=COUNTRY, default='-')
    region = models.CharField(max_length=200, blank=True)
    purchase = models.DateField(blank=True, null=True, auto_now=False, auto_now_add=False)
    price = models.CharField(max_length=12, blank=True, default=0)
    dealer = models.CharField(max_length=200, blank=True)
    drinkfrom = models.IntegerField(blank=True, null=True)
    drinkto = models.IntegerField(blank=True, null=True)
    nmbrbottles = models.IntegerField(default=0)
    warehouse = models.CharField(max_length=200, blank=True)
    notes = models.CharField(max_length=400, blank=True)
    editdate = models.DateField(auto_now=True)


    class Meta:
        ordering = ["drinkto", "country", "region", "year"]

    def get_absolute_url(self):
        return reverse('wine-detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.text

