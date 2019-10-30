from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import  UserCreationForm


class UserRegistrationForm(UserCreationForm):
    first_name = forms.CharField(max_length = 60)
    last_name = forms.CharField(max_length = 60)
    email = forms.EmailField(max_length = 60)

    class Meta:
        model = User
        fields =['first_name','last_name','username', 'email', 'password1', 'password2']
