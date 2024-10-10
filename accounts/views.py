""" This file is used to create views for the accounts app. """

from django.shortcuts import redirect, render
from django.contrib import messages
from django.views import View
from django.contrib.auth import authenticate, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import UserLoginForm, UserRegistrationForm


# def register(request):
#     if request.method == "POST":
#         form = UserRegistrationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect("login")
#     else:
#         form = UserRegistrationForm()
#     context = {
#         "form": form,
#         "title": "Register User",
#     }
#     return render(request, "accounts/register.html", context=context)

class RegisterView(View):
    """This class-based view handles user registration."""

    def get(self, request):
        """Handles GET requests to the register view."""
        form = UserRegistrationForm()
        context = {
            "form": form,
            "title": "Register User",
        }
        return render(request, "accounts/register.html", context=context)

    def post(self, request):
        """Handles POST requests to the register view."""
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account created successfully. Please Contact admin for account activation.")
            return redirect("login")
        context = {
            "form": form,
            "title": "Register User",
        }
        return render(request, "accounts/register.html", context=context)


class LoginView(View):
    """This class-based view handles user login."""

    template_name = "accounts/login.html"

    def get(self, request):
        """Handles GET requests to the login view."""
        form = UserLoginForm()
        context = {
            "form": form,
            "title": "Login",
        }
        return render(request, self.template_name, context=context)

    def post(self, request):
        """Handles POST requests to the login view."""
        form = UserLoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get("email")
            password = form.cleaned_data.get("password")
            user = authenticate(email=email, password=password)
            if user is None:
                messages.error(request, "Invalid email or password.")
                return redirect("login")
            if not user.is_active:
                messages.error(request, "Account is not active. Please contact admin.")
                return redirect("login")
            messages.success(request, "Login successful.")
            return redirect("home")
        context = {
            "form": form,
            "title": "Login",
        }
        return render(request, "accounts/login.html", context=context)

class LogoutView(LoginRequiredMixin, View):
    """ This class-based view handles user logout. """

    def get(self, request):
        """ Handles GET requests to the logout view. """
        logout(request)
        messages.success(request, "You are logged out successfully.")
        return redirect("login")
