""" This module defines the forms used in the accounts app."""

from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

User = get_user_model()


class CustomUserCreationForm(UserCreationForm):
    """This class defines the form for creating a new user"""

    class Meta(UserCreationForm.Meta):
        """This class defines the metadata for the CustomUserCreationForm"""

        model = User
        fields = [
            "email",
            "first_name",
            "last_name",
            "role",
            "password1",
            "password2",
            "is_active",
            "is_staff",
            "is_superuser",
            "groups",
            "user_permissions",
        ]


class CustomUserChangeForm(UserChangeForm):
    """This class defines the form for updating a user"""

    class Meta(UserChangeForm.Meta):
        """This class defines the metadata for the CustomUserChangeForm"""

        model = User
        fields = [
            "email",
            "first_name",
            "last_name",
            "role",
            "password",
            "is_active",
            "is_staff",
            "is_superuser",
            "groups",
            "user_permissions",
        ]


class UserRegistrationForm(UserCreationForm):
    """This class defines the form for creating a new user"""

    class Meta(UserCreationForm.Meta):
        """This class defines the metadata for the CustomUserCreationForm"""

        model = User
        fields = [
            "email",
            "first_name",
            "last_name",
            "password1",
            "password2",
        ]

    def __init__(self, *args, **kwargs):
        super(UserRegistrationForm, self).__init__(*args, **kwargs)
        for _, field in self.fields.items():
            existing_classes = field.widget.attrs.get("class", "")
            field.widget.attrs["class"] = f"form-control {existing_classes}"

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_active = False
        if commit:
            user.save()
        return user


class UserLoginForm(forms.Form):
    """This class defines the form for logging in a user"""

    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={"class": "form-control", "placeholder": "Email"}
        ),
        label="Email",
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={"class": "form-control", "placeholder": "Password"}
        ),
        label="Password",
    )
