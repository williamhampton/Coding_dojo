from django import forms
from .models import age
from django.forms import extras

class registration(forms.Form):
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    email = forms.EmailField()
    age = forms.IntegerField()
