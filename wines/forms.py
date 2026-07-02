from django import forms
from .models import Wine
from datetime import datetime


class WineForm(forms.ModelForm):

    class Meta:
        model = Wine
        current_year = datetime.now().year

        fields = [
            'winename', 'producer', 'country', 'region', 'year',
            'winetype', 'grapes', 'purchase', 'dealer',
            'price', 'drinkfrom', 'drinkto',
            'warehouse', 'notes', 'nmbrbottles'
        ]

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
            'winename': forms.TextInput(),
            'producer': forms.TextInput(),
            'grapes': forms.TextInput(),
            'winetype': forms.Select(),
            'year': forms.NumberInput(attrs={'min': '1990', 'max': '2025'}),
            'country': forms.Select(),
            'region': forms.TextInput(),
            'purchase': forms.DateInput(
                format='%Y-%m-%d',
                attrs={
                    'type': 'date',
                    'class': 'w-full md:w-auto'}
            ),
            'price': forms.TextInput(),
            'dealer': forms.TextInput(),
            'notes': forms.Textarea(attrs={'rows': 15}),
            'drinkfrom': forms.NumberInput(attrs={'min': '2000', 'max': '2060'}),
            'drinkto': forms.NumberInput(attrs={'min': '2018', 'max': '2065'}),
            'warehouse': forms.TextInput(),
            'nmbrbottles': forms.NumberInput(
                attrs={
                    'type': 'range',
                    'min': '0',
                    'max': '18',
                }
            ),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        input_class = (
            "w-full rounded-xl border border-gray-300 "
            "px-3 py-2 text-sm "
            "focus:outline-none focus:ring-2 focus:ring-gray-300"
        )

        for name, field in self.fields.items():
            if name != "nmbrbottles":
                field.widget.attrs.update({
                    "class": input_class
                })

        self.fields["purchase"].widget.attrs["class"] = (
            "w-80 rounded-xl border border-gray-300 "
            "px-3 py-2 text-sm "
            "focus:outline-none focus:ring-2 focus:ring-gray-300"
        )

        self.fields["nmbrbottles"].widget.attrs.update({
            "class": (
                "w-full h-2 rounded-lg "
                "accent-gray-700"
            )
        })
