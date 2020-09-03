from django import forms
from .models import Inventory

class ItemForm(forms.ModelForm):
    class Meta:
        model = Inventory
        fields = [
            #'name',
            'gtin',
            'expiry_date']
        