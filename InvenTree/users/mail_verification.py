from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.core.exceptions import ValidationError
from django.utils import six
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.contrib.auth import get_user_model

User = get_user_model()


class AccountActivationTokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, user, timestamp):
        return (
            six.text_type(user.pk) + six.text_type(timestamp) +
            six.text_type(user.is_active)
        )


class UserTokenVerification(AccountActivationTokenGenerator):
    def generate_uid_token(self, user):
        token = self.make_token(user)
        uid = urlsafe_base64_encode(force_bytes(user.pk))
        return [uid, token]

    def validate_uid_token(self, uid, token):
        user = self.get_user(uid)
        if user:
            if self.check_token(user, token):
                return user
        return False

    def get_user(self, uid):
        try:
            uid = urlsafe_base64_decode(uid).decode()
            user = User.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, User.DoesNotExist, ValidationError):
            user = None
        return user


utv = UserTokenVerification()
def get_token_generator():
    return utv

