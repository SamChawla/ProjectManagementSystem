""" This module contains the models for the accounts app """

from enum import StrEnum

from django.contrib.auth.base_user import BaseUserManager

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

class UserRoles(StrEnum):
    """ This class defines the User Roles """
    ADMIN = "Admin"
    PROJECT_MANAGER = "Project Manager"
    TEAM_MEMBER = "Team Member"

class CustomUserManager(BaseUserManager):
    """" This class defines custom user manager for CustomUser Model """

    def create_user(self, email, password=None, **extra_fields):
        """ Create and return a regular user with user object 
        
        Args:
            email (str) : Email of the user
            password (str) : password of the user
            **extra_fields : Extra fields for the user
        
        Returns:
            _type : CustomUser
        
        """
        if not email:
            raise ValueError("The Email field should be set.")
        import pdb;pdb.set_trace()
        email = self.normalize_email(email)
        user = self.model(email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        """ Create and return a admin user with user object 
        
        Args:
            email (str) : Email of the user
            password (str) : password of the user
            **extra_fields : Extra fields for the user
        
        Returns:
            _type : CustomUser
        """
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("role", UserRoles.ADMIN)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")
        if extra_fields.get("role") != UserRoles.ADMIN:
            raise ValueError("Superuser must have role=ADMIN.")

        return self.create_user(email, password, **extra_fields)


class CustomUser(AbstractUser):
    """
    Custom User within the Django authentication system are represented by this
    model.

    email and password are required. Other fields are optional.
    """
    username = None
    email = models.EmailField(_("email address"), unique=True)
    profile_picture = models.ImageField(upload_to="profile_pictures", blank= True, null=True)
    role = models.CharField(max_length=20, choices=[(role.value, role.value) for role in UserRoles], default= UserRoles.TEAM_MEMBER)
    
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name"]

    objects = CustomUserManager()
    
    def __str__(self):
        return f"{self.id} - {self.get_full_name()}"
    








