# forms.py
from django import forms
from .models import Menu

class CoffeesForm(forms.ModelForm):
    class Meta:
        model = Menu
        fields = ['name', 'description', 'price', 'category', 'image']