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

class ProfileInfoForm(forms.ModelForm):
    street_name = forms.CharField(max_length = 60)
    house_nr = forms.IntegerField()
    addition = forms.CharField(max_length = 60, required = False)
    house_nr = forms.CharField(max_length = 60)
    postcode = forms.CharField(max_length = 60)
    city = forms.CharField(max_length = 60)
    country = forms.CharField(label="Country:", widget=forms.Select(choices=[('netherland','Netherland'),('usa','USA'),('germany','Germany'),('uk','United Kingdom')]))
    language = forms.CharField(label="Language:", widget=forms.Select(choices=[('english','English'),('dutch','Dutch')]))
    class Meta:
        model = UserProfile
        fields = ['street_name','house_nr','addition','house_nr','postcode','city','country','language']
