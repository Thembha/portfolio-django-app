from django import forms
from django.contrib.auth.models import User
from .models import Profile
from django.contrib.auth.forms import UserCreationForm

class RegisterForm(UserCreationForm):
    first_name = forms.CharField(
                    max_length=100,required=True,widget=forms.TextInput(attrs={'placeholder': 'First Name','class': 'form-control textbox',})
                )
    last_name = forms.CharField(
                    max_length=100,required=True,widget=forms.TextInput(attrs={'placeholder': 'Last Name','class': 'form-control textbox',})
                )
    username = forms.CharField(
                    max_length=100,required=True,widget=forms.TextInput(attrs={'placeholder': 'Username','class': 'form-control textbox',})
                )
    email = forms.EmailField(
                required=True,widget=forms.EmailInput(attrs={'placeholder': 'Email','class': 'form-control textbox',})
            )
    phone_number = forms.CharField(widget=forms.NumberInput(attrs={'placeholder': 'Phone Number','class': 'form-control textbox'}))
    home_address = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Home Address','class': 'form-control', 'rows': 4}))
    # location input boxes MUST have ids 'lat' and 'lon' respectively, otherwise the get_current_location script will cause a js error.
    location_lat = forms.DecimalField(widget=forms.NumberInput(attrs={'placeholder': 'Lattitude','id':'lat','class': 'form-control textbox'}))
    location_lon = forms.DecimalField(widget=forms.NumberInput(attrs={'placeholder': 'Longitude','id':'lon','class': 'form-control textbox'}))
    
    password1 = forms.CharField(
                    max_length=50,required=True,widget=forms.PasswordInput(
                            attrs={'placeholder': 'Password','class': 'form-control textbox',
                            'data-toggle': 'password','id': 'password',}
                        )
                )
    password2 = forms.CharField(
                    max_length=50,required=True,widget=forms.PasswordInput(
                        attrs={'placeholder': 'Confirm Password','class': 'form-control textbox',
                        'data-toggle': 'password','id': 'password',}
                    )
                )

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'phone_number','home_address','location_lat','location_lon','password1', 'password2']



class UpdateUserForm(forms.ModelForm):
    username = forms.CharField(max_length=100,required=True,widget=forms.TextInput(attrs={'class': 'form-control textbox'}))
    first_name = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control textbox'}))
    last_name = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control textbox'}))
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class': 'form-control textbox'}))

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']


class UpdateProfileForm(forms.ModelForm):
    phone_number = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control textbox'}))
    home_address = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 4}))
    location_lat = forms.DecimalField(widget=forms.NumberInput(attrs={'id':'lat','class': 'form-control textbox'}))
    location_lon = forms.DecimalField(widget=forms.NumberInput(attrs={'id':'lon','class': 'form-control textbox'}))
    
    class Meta:

        model = Profile
        fields = ['phone_number', 'home_address','location_lat','location_lon']

