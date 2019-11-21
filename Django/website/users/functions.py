from django.core.mail import send_mail
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from validate_email import validate_email
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from users.tokens import account_activation_token
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_text
from django.core.mail import EmailMessage



def send_confirmation_email(request, form, user, user_email):
    current_site = get_current_site(request)
    mail_subject = 'Activate your blog account.'
    message = render_to_string('acc_active_email.html', {
        'user': user,
        'domain': current_site.domain,
        'uid':urlsafe_base64_encode(force_bytes(user.pk)),
        'token':account_activation_token.make_token(user),
    })
    print(message)
    
    send_mail(
        mail_subject,
        message,
        'artdrop.project@gmail.com',
        [user_email],
    )
    

def check_email_alrady_used(email):
#     if User.objects.filter(email=email).exists():
#         raise ValidationError("Account with this email already exists.")
#     return self.cleaned_data
#     # return email
    pass
