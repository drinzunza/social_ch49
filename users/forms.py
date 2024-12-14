from django import forms
from django.contrib.auth.models import User
from .models import Profile

class SignupForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password']



class ProfileForm(forms.ModelForm):
    
    class Meta:
        model = Profile
        fields = ['avatar', 'phone_number', 'street', 'city', 'state', 'zip_code']