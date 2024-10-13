""" This modules contains the urls for the accounts app."""

from django.urls import path
from accounts.views import RegisterView


urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
]