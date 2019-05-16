from django import forms
from .models import DataItem

class dataItemForm(forms.ModelForm):
    class Meta:
        model= DataItem
        fields= ["id", "lastprice", "sinceclose", "sinceopen", "name", "isin", "place"]