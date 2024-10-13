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


class UserRegistrationForm(UserCreationForm):
    """This class defines the form for creating a new user via UI"""

    class Meta(UserCreationForm.Meta):
        """This class defines the metadata for the UserRegistrationForm"""

        model = User
        fields = [
            "email",
            "first_name",
            "last_name",
            "role",
            "password1",
            "password2",
        ]

    def __init__(self, *args, **kwargs):
        """This method initializes the UserRegistrationForm"""
        super().__init__(*args, **kwargs)
        self.fields["email"].widget.attrs.update(
            {"autofocus": True, "placeholder": "Email", "class": "form-control"}
        )
        self.fields["first_name"].widget.attrs.update(
            {"autofocus": True, "placeholder": "First Name", "class": "form-control"}
        )
        self.fields["last_name"].widget.attrs.update(
            {"autofocus": True, "placeholder": "Last Name", "class": "form-control"}
        )
        self.fields["role"].widget.attrs.update(
            {"autofocus": True, "placeholder": "Role", "class": "form-control"}
        )
        self.fields["password1"].widget.attrs.update(
            {"autofocus": True, "placeholder": "Password", "class": "form-control"}
        )
        self.fields["password2"].widget.attrs.update(
            {
                "autofocus": True,
                "placeholder": "Confirm Password",
                "class": "form-control",
            }
        )

    def save(self, commit=True):
        """This method saves the user to the database"""
        user = super().save(commit=False)
        user.is_active = False
        if commit:
            user.save()
        return user


class UserLoginForm(UserCreationForm):
    """This class defines the form for logging in a user"""

    class Meta(UserCreationForm.Meta):
        """This class defines the metadata for the UserLoginForm"""

        model = User
        fields = [
            "email",
            "password",
        ]

    def __init__(self, *args, **kwargs):
        """This method initializes the UserLoginForm"""
        super().__init__(*args, **kwargs)
        self.fields["email"].widget.attrs.update(
            {"autofocus": True, "placeholder": "Email", "class": "form-control"}
        )
        self.fields["password"].widget.attrs.update(
            {"autofocus": True, "placeholder": "Password", "class": "form-control"}
        )
