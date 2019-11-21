from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegistrationForm, UserUpdateForm, ProfilePhotoUpdateForm, ProfileInfoForm
from django.contrib.auth.decorators import login_required
from .functions import send_confirmation_email

from django.http import HttpResponse
from django.contrib.auth import login, authenticate
# from .forms import SignupForm
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.contrib.auth.models import User
from django.core.mail import EmailMessage

from django.core.mail import send_mail
from django.core.exceptions import ValidationError
from django import forms


# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            if User.objects.filter(email=email).exists():
                # raise forms.ValidationError("Account with this email already exists.")
                messages.warning(request, f'An account with this email already exists')
                return render(request,'users/register.html',{'form':form})

            else:
                user = form.save(commit=False)
                user.is_active = False
                user.save()
                # user = form.save()
                username = form.cleaned_data.get('username')
                messages.success(request, f'account created for {username}')
                
                print(email)
                send_confirmation_email(request, form, user, email)
                
            return redirect('login_page')
        # return HttpResponse('Please confirm your email address to complete the registration')
    else:
        form = UserRegistrationForm()
    return render(request,'users/register.html',{'form':form})

def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        # return redirect('home')
        return render(request,'email/confirmation_complete.html')
    else:
        return render(request,'email/invalid_link.html')

@login_required
def profile(request):
    if request.method == 'POST':
        user_update_form = UserUpdateForm(request.POST,instance=request.user)
        profile_photo_update_form = ProfilePhotoUpdateForm(request.POST,request.FILES,
                                                        instance=request.user.userprofile)
        profile_info_update_form = ProfileInfoForm(request.POST,instance=request.user.userprofile)
        if user_update_form.is_valid and profile_photo_update_form.is_valid and profile_info_update_form.is_valid:
            user_update_form.save()
            profile_info_update_form.save()
            profile_photo_update_form.save()
            messages.success(request, f'Your profile information is updated')
            return redirect('profile_page')

    else:
        user_update_form = UserUpdateForm(instance=request.user)
        profile_info_update_form = ProfileInfoForm(instance=request.user.userprofile)
        profile_photo_update_form = ProfilePhotoUpdateForm(instance=request.user.userprofile)
    context ={
        'user_update_form': user_update_form,
        'profile_photo_update_form': profile_photo_update_form,
        'profile_info_update_form': profile_info_update_form
    }
    return render(request, 'users/profile.html', context)
