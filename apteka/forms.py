
from django import forms

class AptekaForm(forms.Form):
    name = forms.CharField(max_length = 100)
    phone = forms.CharField(max_length=15)
    address = forms.CharField(max_length = 100)
    latitude = forms.CharField(max_length = 50)
    longitude = forms.CharField(max_length = 50)
