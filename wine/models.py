from django.db import models
from django.urls import reverse
from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User, Group

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
    owner = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
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

    def __str__(self):
        return self.text

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
            'winename': forms.TextInput(attrs={'class': "form-control"}),
            'producer': forms.TextInput(attrs={'class': "form-control"}),
            'grapes': forms.TextInput(attrs={'class': "form-control"}),
            'year': forms.NumberInput(attrs={'class': "form-control", 'min': '1990', 'max': '2021', 'value': '2021'}),
            'country': forms.Select(attrs={'class': "form-control"}),
            'region': forms.TextInput(attrs={'class': "form-control"}),
            'purchase': forms.SelectDateWidget(attrs={'class': "form-control"}, years=range(2010, 2022), empty_label=("Jahr", "Monat", "Tag")),
            'price': forms.TextInput(attrs={'class': "form-control"}),
            'dealer': forms.TextInput(attrs={'class': "form-control"}),
            'notes': forms.Textarea(attrs={'class': "form-control", 'cols': 100, 'rows': 5}),
            'drinkfrom': forms.NumberInput(attrs={'class': "form-control", 'min': '2000', 'max': '2060', 'type': 'number'}),
            'drinkto': forms.NumberInput(attrs={'class': "form-control", 'min': '2018', 'max': '2060', 'type': 'number'}),
            'nmbrbottles': forms.NumberInput(attrs={'class': "form-control"}),

        }