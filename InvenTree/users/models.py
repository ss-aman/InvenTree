# from django.contrib.auth.models import AbstractUser 
# from django.core.mail import send_mail

# from django.db import models


# class User(AbstractUser):
#     email = models.EmailField(unique=True,
#                               error_messages={
#                                   'unique': "A user with that email already exists.",
#                               },
#                               )

#     company = models.ForeignKey('company.Company', blank=True, null=True, on_delete=models.CASCADE)
#     job_role = models.CharField(max_length=50, blank=True, null=True)

#     def email_user(self, subject, message, from_email=None, **kwargs):
#         send_mail(subject, message, from_email, [self.email], **kwargs)

#     class Meta(AbstractUser.Meta):
#         pass
