from django import forms
from .models import Users

class registration(forms.ModelForm):
#    first_name = forms.CharField(max_length=100)
#    last_name = forms.CharField(max_length=100)
#    email = forms.EmailField()
#    password = forms.CharField(max_length=100, widget=forms.PasswordInput)
#    confirm_password =forms.CharField(max_length=100, widget=forms.PasswordInput)
    confirm_password = forms.CharField(max_length=100, widget=forms.PasswordInput)
    class Meta:
        model = Users
        fields = '__all__'
