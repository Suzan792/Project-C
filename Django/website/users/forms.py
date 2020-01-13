from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User

from .functions import check_email_already_used
from .models import UserProfile, isArtist


class UpdatedLoginForm(AuthenticationForm):
    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username is not None and password:
            self.user_cache = authenticate(self.request, username=username, password=password)
            if self.user_cache is None:
                try:
                    user_temp = User.objects.get(username=username, is_active=False)
                except:
                    user_temp = None
                if user_temp is not None:
                    raise forms.ValidationError(
                        self.error_messages['inactive'],
                        code='inactive',
                    )
                else:
                    raise self.get_invalid_login_error()
            else:
                self.confirm_login_allowed(self.user_cache)

        return self.cleaned_data

class UserRegistrationForm(UserCreationForm):
    first_name = forms.CharField(max_length = 60)
    last_name = forms.CharField(max_length = 60)
    email = forms.EmailField(max_length = 60)
    def clean_email(self):
        email = self.cleaned_data.get('email')
        check_email_already_used(email)
        return email
    class Meta:
        model = User
        fields =['first_name','last_name','username', 'email', 'password1', 'password2']

class UserUpdateForm(forms.ModelForm):
    first_name = forms.CharField(max_length = 60)
    last_name = forms.CharField(max_length = 60)
    email = forms.EmailField(max_length = 60)
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if self.instance.email != email:
            check_email_already_used(email)
        return email
    class Meta:
        model = User
        fields =['first_name','last_name','username', 'email']

class ProfilePhotoUpdateForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['image']
class ProfileInfoForm(forms.ModelForm):
    street_name = forms.CharField(max_length = 60, required = False)
    house_number = forms.IntegerField( required = False)
    addition = forms.CharField(max_length = 60, required = False)
    house_number = forms.CharField(max_length = 60, required = False)
    postcode = forms.CharField(max_length = 60, required = False)
    city = forms.CharField(max_length = 60, required = False)
    class Meta:
        model = UserProfile
        fields = ['street_name','house_number','addition','house_number','postcode','city','country','language']


class artistApplication(forms.ModelForm):
    class Meta:
        model = isArtist
        fields = ['applicant_description','artwork_example_title','artwork_example_description','artwork_example_image']
