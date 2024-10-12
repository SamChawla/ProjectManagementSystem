""" This file contains the views for the accounts app."""

from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.views import View
from .forms import UserRegistrationForm, UserLoginForm

User = get_user_model()


# Function Based View
# def register(request):
#     """This function renders the registration form."""
#     if request.method == "POST":
#         form = CustomUserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect("login")
#     else:
#         form = CustomUserCreationForm()
#     return render(request, "registration/register.html", {"form": form})


# Class Based View

class RegisterView(View):
    """This class renders the registration form."""

    def get(self, request):
        """This method handles the GET request."""
        form = UserRegistrationForm()
        return render(request, "accounts/register.html", {"form": form})

    def post(self, request):
        """This method handles the POST request."""
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "User created successfully. Please ask admin to activate your account.")
            return redirect("login")
        return render(request, "accounts/register.html", {"form": form})
