from django import forms
from django.contrib.auth.models import User
from .models import *
from django.forms import TimeInput

class SigninForm(forms.Form):
     username = forms.CharField(max_length=50)
     password = forms.CharField(widget=forms.PasswordInput)

class SignupForm(forms.Form):
     username = forms.CharField(max_length=50)
     phone_number = forms.CharField(max_length=15)
     password = forms.CharField(widget=forms.PasswordInput)

     def clean_username(self):
         username = self.cleaned_data['username']
         if User.objects.filter(username=username).exists():
             raise forms.ValidationError('Username already exists')
         return username




class RideForm(forms.ModelForm):
    class Meta:
        model = Ride
        fields = ['origin', 'destination', 'name',]
     