from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegistrationForm, UserUpdateForm, ProfilePhotoUpdateForm
from django.contrib.auth.decorators import login_required
# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'account created for {username}')
            return redirect('login_page')
    else:
        form = UserRegistrationForm()
    return render(request,'users/register.html',{'form':form})

@login_required
def profile(request):
    if request.method == 'POST':
        user_update_form = UserUpdateForm(request.POST,instance=request.user)
        profile_photo_update_form = ProfilePhotoUpdateForm(request.POST,request.FILES,
                                                        instance=request.user.userprofile)
        if user_update_form.is_valid and profile_photo_update_form.is_valid():
            user_update_form.save()
            profile_photo_update_form.save()
            messages.success(request, f'Your profile information is updated')
            return redirect('profile_page')

    else:
        user_update_form = UserUpdateForm(instance=request.user)
        profile_photo_update_form = ProfilePhotoUpdateForm(instance=request.user.userprofile)
    context ={
        'user_update_form': user_update_form,
        'profile_photo_update_form': profile_photo_update_form
    }
    return render(request, 'users/profile.html', context)
