""" This module is used to register the models with the admin site. """

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from accounts.models import CustomUser
from accounts.forms import CustomUserCreationForm, CustomUserChangeForm


class CustomUserAdmin(UserAdmin):
    """This class defines the custom user admin."""

    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ["email", "first_name", "last_name", "role", "is_active", "is_staff", "is_superuser"]
    list_filter = ["role", "is_active", "is_staff", "is_superuser"]
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        ("Personal info", {"fields": ("first_name", "last_name")}),
        ("Permissions", {"fields": ("role", "is_active", "is_staff", "is_superuser", "groups", "user_permissions")}),
    )
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("email", "password1", "password2", "role", "is_active", "is_staff", "is_superuser", "groups", "user_permissions"),
        }),
    )
    search_fields = ["email", "first_name", "last_name"]
    ordering = ["email"]


admin.site.register(CustomUser, CustomUserAdmin)