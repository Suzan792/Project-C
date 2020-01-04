from datetime import datetime
from django.contrib import messages
from django.contrib.admin.views.decorators import staff_member_required
from django.core.mail import send_mail
from django.utils.decorators import method_decorator
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.utils.encoding import force_text
from django.utils.http import urlsafe_base64_decode
from django.http import HttpResponse
from django.views.generic import DetailView, DeleteView
from art.models import Artwork
from website import settings
from .models import isArtist,UserProfile
from .forms import UserRegistrationForm, UserUpdateForm, ProfilePhotoUpdateForm, ProfileInfoForm , artistApplication
from .functions import send_confirmation_email
from .tokens import account_activation_token
from django.views.generic import ListView
# Create your views here.


class ArtistCard(DetailView):
    model = User
    template_name = 'artistCard.html'

    def get_context_data(self, *args, **kwargs):
        context = super(ArtistCard, self).get_context_data(*args, **kwargs)
        context['User'] = User.objects.all()
        context['Artwork'] = Artwork.objects.all()
        return context


def artist_register_info(request):
    return render(request,'users/info_artist_register.html')


def register(request):
    if request.user.is_authenticated:
        return HttpResponse("you are already logged in!")
    else:
        if request.method == 'POST':
            form = UserRegistrationForm(request.POST)
            if form.is_valid():
                user = form.save(commit=False)
                user.is_active = False
                user.save()
                username = form.cleaned_data.get('username')
                messages.success(request, f'account created for {username}')

                email = form.cleaned_data.get('email')
                send_confirmation_email(request, form, user, email)

                return render(request,'email/email_sent.html')
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
            messages.success(request, f'Your profile information has been updated')
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


@login_required
def isartist(request):
    if isArtist.objects.filter(applicant=request.user.userprofile).exists():
        return HttpResponse("you are already sent a application!")
    else:
        if request.method == 'POST':
            form = artistApplication(request.POST,request.FILES)
            if form.is_valid():
                # save to db
                instance = form.save(commit=False)
                instance.applicant = request.user.userprofile
                instance.save()
                messages.success(request, f'Your application is received, you will receive an answer very quick  ')
                return redirect('home_page')
        else:
            form = artistApplication()
        return render(request, 'isartist.html', {'form': form})


@method_decorator(staff_member_required, name='dispatch')
class artistAllApplications(ListView):
    model = isArtist
    template_name = 'admin/allApplications.html'


@method_decorator(staff_member_required, name='dispatch')
class artistDetailApplications(DetailView):
    model = isArtist
    template_name = 'admin/detailApplications.html'


@method_decorator(staff_member_required, name='dispatch')
class rejectArtistApplication(DeleteView):
    model = isArtist
    template_name = 'admin/deleteApplications.html'
    success_url = '/administrator'

    def delete(self, request, *args, **kwargs):
        subject = 'your application has been rejected'
        message = 'sorry to tell that your request does not meet our requirement so it has been rejected.'
        email_from = settings.EMAIL_HOST_USER
        self.object = self.get_object()
        recipient_list = [self.object.applicant.user.email]
        success_url = self.get_success_url()
        self.object.delete()
        send_mail(subject, message, email_from, recipient_list)
        return redirect('/administrator')


@method_decorator(staff_member_required, name='dispatch')
class approveArtistApplication(DeleteView):
    model = isArtist
    template_name = 'admin/approveApplications.html'
    success_url = '/administrator'

    def delete(self, request, *args, **kwargs):
        subject = 'your application has been approved'
        message = 'Happy to tell that your request has been approved. your artist account has been activated. we are ' \
                  'looking up to see your first artwork '
        email_from = settings.EMAIL_HOST_USER
        self.object = self.get_object()
        recipient_list = [self.object.applicant.user.email]
        UserProfile.objects.filter(user = self.object.applicant.user).update(user_role='artist',activated_artist_date=datetime.now())
        success_url = self.get_success_url()
        self.object.delete()
        send_mail(subject, message, email_from, recipient_list)
        return redirect('/administrator')










