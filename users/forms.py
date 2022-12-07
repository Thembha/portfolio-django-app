from django import forms

from django.contrib.auth.models import User
from .models import Profile


class UpdateUserForm(forms.ModelForm):
    username = forms.CharField(max_length=100,required=True,widget=forms.TextInput(attrs={'class': 'form-control textbox'}))
    first_name = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control textbox'}))
    last_name = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control textbox'}))
    email = forms.EmailField(required=True, widget=forms.TextInput(attrs={'class': 'form-control textbox'}))

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']


class UpdateProfileForm(forms.ModelForm):
    phone_number = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control textbox'}))
    home_address = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 4}))
    location_lat = forms.DecimalField(widget=forms.TextInput(attrs={'class': 'form-control textbox'}))
    location_lon = forms.DecimalField(widget=forms.TextInput(attrs={'class': 'form-control textbox'}))
    
    class Meta:

        model = Profile
        fields = ['phone_number', 'home_address','location_lat','location_lon']

