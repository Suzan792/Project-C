from django.core.mail import send_mail
from django.core.exceptions import ValidationError
from validate_email import validate_email


def check_real_email(email):
    # try:
    #     send_mail(
    #         'Subject here',
    #         'Here is the message.',
    #         'artdrop.project@gmail.com',
    #         [email],
    #         fail_silently=False,
    #     )
    #     return 
    # except ValidationError:
    #     raise ValidationError("This email does not exist.")

    # is_valid = validate_email(email, verify=True)
    if not validate_email(email, verify=True):
        raise ValidationError("This email does not exist.")