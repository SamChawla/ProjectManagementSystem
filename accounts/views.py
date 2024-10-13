""" This file contains the views for the accounts app."""

from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth import get_user_model, login
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
            messages.success(
                request,
                "User created successfully. Please ask admin to activate your account.",
            )
            return redirect("login")
        return render(request, "accounts/register.html", {"form": form})


class LoginView(View):
    """This class renders the login form."""

    def get(self, request):
        """This method handles the GET request."""
        form = UserLoginForm()
        return render(request, "accounts/login.html", {"form": form})

    def post(self, request):
        """This method handles the POST request."""
        form = UserLoginForm(request.POST)

        if form.is_valid():
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]

            user = User.objects.filter(email=email).first()

            if user is None:
                messages.error(request, "Invalid email.")
                return redirect("login")
            if not user.is_active:
                messages.error(request, "User is not active. Please contact admin.")
                return redirect("login")
            if not user.check_password(password):
                messages.error(request, "Invalid password.")
                return redirect("login")

            login(request, user)
            return redirect("home")

        return render(request, "accounts/login.html", {"form": form})


class DashboardView(View):
    """This class renders the dashboard view."""

    def get(self, request):
        """This method handles the GET request."""
        return render(request, "accounts/dashboard.html")
