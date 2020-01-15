from django.contrib.auth.models import AbstractUser 
from django.core.mail import send_mail

from django.db import models



EMPLOYEE_TYPES = {

}

class User(AbstractUser):
    email = models.EmailField(unique=True,
                              error_messages={
                                  'unique': "A user with that email already exists.",
                              },
                              )

    job_role = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)

    def email_user(self, subject, message, from_email=None, **kwargs):
        send_mail(subject, message, from_email, [self.email], **kwargs)

    # class Meta(AbstractUser.Meta):
    #     pass
