from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import User
from .widgets import ChangedClearableFileInput


class HaskerUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = (
            "username",
            "email",
            "avatar",
        )


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = (
            "email",
            "avatar",
        )
        widgets = {
            'avatar': ChangedClearableFileInput(),
        }
