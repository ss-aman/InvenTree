from django.contrib.auth.models import AbstractUser 
from django.core.mail import send_mail
from django.contrib import admin

from django.db import models



JOB_ROLES = (
    ('SUPPLIER', 'SUPPLIER'),
    ('COMPANY', 'SUPPLIER'),
    ('ADMIN', 'ADMIN'),
    ('EMPLOYEE', 'EMPLOYEE'),
)

ACTIVE_STATUS = (
    (True, 'active'),
    (False, 'in_active'),
)

class User(AbstractUser):
    email = models.EmailField(unique=True,
                              error_messages={
                                  'unique': "A user with that email already exists.",
                              },
                              )
    is_active = models.BooleanField()

    def email_user(self, subject, message, from_email=None, **kwargs):
        send_mail(subject, message, from_email, [self.email], **kwargs)
