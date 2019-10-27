from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import  UserCreationForm


class UserRegistrationForm(UserCreationForm):
    firstname = forms.CharField(max_length = 60)
    lastname = forms.CharField(max_length = 60)
    email = forms.EmailField(max_length = 60)

    class Meta:
        model = User
        fields =['firstname','lastname','username', 'email', 'password1', 'password2']
