from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import  UserCreationForm
from .models import UserProfile


class UserRegistrationForm(UserCreationForm):
    first_name = forms.CharField(max_length = 60)
    last_name = forms.CharField(max_length = 60)
    email = forms.EmailField(max_length = 60)

    class Meta:
        model = User
        fields =['first_name','last_name','username', 'email', 'password1', 'password2']

class UserUpdateForm(forms.ModelForm):
    first_name = forms.CharField(max_length = 60)
    last_name = forms.CharField(max_length = 60)
    email = forms.EmailField(max_length = 60)

    class Meta:
        model = User
        fields =['first_name','last_name','username', 'email']

class ProfilePhotoUpdateForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['image']
