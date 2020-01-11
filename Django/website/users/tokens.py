from django.contrib.auth.tokens import PasswordResetTokenGenerator
# from django.utils import six #TODO check if this works
# import users.django_six as six
class TokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, user, timestamp):
        return (
            six.text_type(user.pk) + six.text_type(timestamp) +
            six.text_type(user.is_active)
        )
account_activation_token = TokenGenerator()

# source: https://medium.com/@frfahim/django-registration-with-confirmation-email-bb5da011e4ef
