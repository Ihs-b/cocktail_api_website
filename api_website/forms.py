from django import forms


class AlcoholForm(forms.Form):
    alcohol = forms.CharField(label='What is the alcohol you have', min_length=3)