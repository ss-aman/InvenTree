from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm as AuthUserCreationForm


User = get_user_model()

class UserCreationForm(AuthUserCreationForm):
    job_role = forms.CharField()

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email')