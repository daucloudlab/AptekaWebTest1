# *-* coding:utf-8 *-*
from django import forms

class MedikamentForm(forms.Form):
    title = forms.CharField(max_length = 100)
    description = forms.CharField(max_length=100)
    price = forms.CharField(max_length=10)
    CATEGORY_DATA = (
        (1,"Лекарственные преператы"),
        (2,"Для мам"),
        (3,"витамины"),
        (4,"роро"),
        (5,"зщззщз"),
        (6,"dffgg"),
        (7,"uuio"),
        (8,"88909"),
    )
    category = forms.ChoiceField(choices=CATEGORY_DATA)

