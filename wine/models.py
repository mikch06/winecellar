from django.db import models
from django.urls import reverse
from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from datetime import datetime

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

class WineForm(ModelForm):
    class Meta:
        model = Wine
        current_year = datetime.now().year
        fields = ['winename', 'producer', 'country', 'region', 'year', 'winetype', 'grapes', 'purchase', 'dealer',
                  'price', 'drinkfrom', 'drinkto', 'warehouse', 'notes', 'nmbrbottles']
        labels = {
            'winename': 'Weinname',
            'producer': 'Produzent',
            'winetype': 'Weintyp',
            'grapes': 'Trauben',
            'year': 'Jahrgang',
            'country': 'Land',
            'region': 'Region',
            'purchase': 'Kaufdatum',
            'price': 'Preis (~CHF)',
            'dealer': 'Verkäufer',
            'drinkfrom': 'Trinkbar ab',
            'drinkto': 'Trinkbar bis',
            'warehouse': 'Lagerort',
            'nmbrbottles': 'Anzahl Flaschen',
            }

        widgets = {
            'winename': forms.TextInput(attrs={'class': "form-control"}),
            'producer': forms.TextInput(attrs={'class': "form-control"}),
            'grapes': forms.TextInput(attrs={'class': "form-control"}),
            'winetype': forms.Select(attrs={'class': "form-control"}),
            'year': forms.NumberInput(attrs={'class': "form-control", 'min': '1990', 'max': '2025'}),
            'country': forms.Select(attrs={'class': "form-control"}),
            'region': forms.TextInput(attrs={'class': "form-control"}),
            'purchase': forms.DateInput(format=('%Y-%m-%d'), attrs={"type": "date", 'class': "form-control"}),
            'price': forms.TextInput(attrs={'class': "form-control"}),
            'dealer': forms.TextInput(attrs={'class': "form-control"}),
            'notes': forms.Textarea(attrs={'class': "form-control", 'cols': 100, 'rows': 5}),
            'drinkfrom': forms.NumberInput(attrs={'class': "form-control", 'min': '2000', 'max': '2060'}),
            'drinkto': forms.NumberInput(attrs={'class': "form-control", 'min': '2018', 'max': '2060', 'type': 'number'}),
            'warehouse': forms.TextInput(attrs={'class': "form-control"}),
            'nmbrbottles': forms.NumberInput(attrs={'class': "form-range", 'type': 'range', 'min': '0', 'max': '18'}),
        }
