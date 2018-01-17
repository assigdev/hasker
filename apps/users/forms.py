from django.contrib.auth.forms import UserCreationForm
from .models import User
from django import forms


class HaskerUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = (
            "username",
            "nickname",
            "email",
            "avatar",
        )