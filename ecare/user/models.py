from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin, UserManager
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.db import models

from ecare.core.models import AbstractBaseModel


class User(PermissionsMixin, AbstractBaseUser, AbstractBaseModel):
    USERNAME_FIELD = "username"
    EMAIL_FIELD = "email"
    REQUIRED_FIELDS = ["email"]

    username_validator = UnicodeUsernameValidator()

    username = models.CharField(
        "Username",
        max_length=255,
        unique=True,
        validators=[username_validator],
    )
    is_active = models.BooleanField("Active", default=True)

    objects = UserManager()

    # Django-user related fields #
    # password is inherited from AbstractBaseUser
    email = models.EmailField("Email address", blank=True)  # allow non-unique emails
    is_staff = models.BooleanField(
        "staff status",
        default=False,
        help_text="Designates whether the user can log into this admin site.",
    )
