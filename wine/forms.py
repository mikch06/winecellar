from django import forms



class WineForm(forms.Form):
    winename = forms.CharField(label='Weinname prost', max_length=20)
    # purchase = forms.DateField(widget=DateInput)
