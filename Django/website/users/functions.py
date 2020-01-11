from django.core.mail import send_mail
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.contrib.sites.shortcuts import get_current_site
from django.shortcuts import redirect
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes

def send_confirmation_email(request, form, user, user_email):
    current_site = get_current_site(request)
    mail_subject = 'Activate your account.'
    message = render_to_string('email/activate_email.html', {
        'user': user,
        'domain': current_site.domain,
        'uid':urlsafe_base64_encode(force_bytes(user.pk)),
        'token':activation_token.make_token(user),
    })

    send_mail(
        mail_subject,
        message,
        'artdrop.project@gmail.com',
        [user_email],
    )

class TokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, user, time):
        return (str(user.pk) + str(time) + str(user.is_active))
activation_token = TokenGenerator()

def deactivate_account(request):
    '''
    This function deactivates a logged in user's account and sends an email to the account's owner.
    '''
    user = request.user
    user.is_active = False
    user.save()
    
    user_email = request.user.email
    current_site = get_current_site(request)
    mail_subject = 'Your account has been deactivated.'
    message = 'Your account has been deactivated. If you ever want to reactivate your account, you can send an email to artdrop.project@gmail.com.'

    send_mail(
        mail_subject,
        message,
        'artdrop.project@gmail.com',
        [user_email],
    )

    messages.success(request, f'Your account has been deactivated.')

    # logout(request)
   