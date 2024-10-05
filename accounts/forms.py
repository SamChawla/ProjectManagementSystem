""" This module defines the forms used in the accounts app."""

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
