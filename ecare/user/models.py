from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin, UserManager
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.db import models

from ecare.core.models import AbstractBaseModel
from ecare.role.models import Role


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
    email = models.EmailField("Email address", blank=True, unique=True)
    is_staff = models.BooleanField(
        "staff status",
        default=False,
        help_text="Designates whether the user can log into this admin site.",
    )

    MALE = "male"
    FEMALE = "female"
    OTHER = "other"

    GENDER_OPTIONS = [
        (MALE, "Male"),
        (FEMALE, "Female"),
        (OTHER, "Other"),
    ]
    gender = models.CharField(
        "Gender", max_length=255, choices=GENDER_OPTIONS, default=None, null=True
    )
    legalName = models.CharField("Legal Name", max_length=255, default=None, null=True)
    dateOfBirth = models.DateField(default=None, null=True)
    emergencyContact = models.EmailField(default=None, null=True)
    governmentId = models.URLField(default=None, null=True)
    profileImage = models.URLField(default=None, null=True)
    role = models.ForeignKey(Role, default=None, on_delete=models.PROTECT, null=True)

    @property
    def roleType(self):
        return self.role and self.role.type
