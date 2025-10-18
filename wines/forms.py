from django import forms
from .models import Wine
from datetime import datetime



class WineForm(forms.ModelForm):
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
