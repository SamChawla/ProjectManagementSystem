""" This module defines the forms used in the accounts app."""

from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from accounts.models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    """This class defines the form for creating a custom user."""

    class Meta:
        """This class defines the metadata for the custom user creation form."""

        model = CustomUser
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
    """This class defines the form for changing a custom user."""

    class Meta:
        """This class defines the metadata for the custom user change form."""

        model = CustomUser
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