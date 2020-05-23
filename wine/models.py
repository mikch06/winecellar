from django.db import models
from django.urls import reverse
from django import forms
from django.forms import ModelForm

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
class Wine(models.Model):
    winename = models.CharField(max_length=200)
    producer = models.CharField(max_length=200, blank=True)
    grapes = models.CharField(max_length=200, blank=True,)
    year = models.IntegerField(blank=True, null=True)
    country = models.CharField(max_length=12, blank=True, choices=COUNTRY)
    region = models.CharField(max_length=200, blank=True)
    purchase = models.DateField(blank=True, null=True, auto_now=False, auto_now_add=False)
    price = models.CharField(max_length=12, blank=True, default=0)
    dealer = models.CharField(max_length=200, blank=True)
    drinkfrom = models.IntegerField(blank=True, null=True)
    drinkto = models.IntegerField(blank=True, null=True)
    nmbrbottles = models.IntegerField(default=0)
    notes = models.CharField(max_length=400, blank=True)
    editdate = models.DateField(auto_now=True)

    class Meta:
        ordering = ["country", "region", "year"]

    def get_absolute_url(self):
        return reverse('wine-detail', kwargs={'pk': self.pk})

class WineForm(ModelForm):
    class Meta:
        model = Wine
        fields = ['winename', 'producer', 'country', 'region', 'year', 'grapes', 'purchase', 'dealer',
                  'price', 'drinkfrom', 'drinkto', 'nmbrbottles', 'notes']
        labels = {
            'winename': 'Weinname',
            'producer': 'Produzent',
            'grapes': 'Trauben',
            'year': 'Jahrgang',
            'country': 'Land',
            'region': 'Region',
            'purchase': 'Kaufdatum',
            'price': 'Preis (~CHF)',
            'dealer': 'Verkäufer',
            'drinkfrom': 'Trinkbar ab',
            'drinkto': 'Trinkbar bis',
            'nmbrbottles': 'Anzahl Flaschen',
            }

        widgets = {
            'purchase': forms.SelectDateWidget(years=range(2010, 2030),empty_label=("Jahr", "Monat", "Tag")),
            'notes': forms.Textarea(attrs={'cols': 100, 'rows': 5}),
            'year': forms.NumberInput(attrs={'min': '2005', 'max': '2019', 'type': 'number'}),
            'drinkfrom': forms.NumberInput(attrs={'min': '2015','max': '2060','type': 'number'}),
            'drinkto': forms.NumberInput(attrs={'min': '2018', 'max': '2060', 'type': 'number'}),
        }
