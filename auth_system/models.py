# Register your models here.
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from core.models import BaseCustomAuthModel
from core.validators import _PHONE_REGEX
from core.enums import Enums
from django.utils.translation import gettext_lazy as _

class CustomUserManager(BaseUserManager):
    """_summary_

    """
    def create_user(self, email, password=None, **extra_fields):
        """_summary_

        """
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        """_summary_

        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(email, password, **extra_fields)

class CustomUser(AbstractBaseUser, PermissionsMixin, BaseCustomAuthModel):
    """_summary_

    """
    USER_TYPE_CHOICES = (
        (Enums.REGULAR_USER.value, 'Regular User'),
        (Enums.ADMIN_USER.value, 'Administrator'),
        # Add other user types as needed
    )

    GENDER_CHOICES = (
        ("male", 'Male'),
        ("female", 'Female')
    )

    user_type = models.PositiveSmallIntegerField(_('User Type'), choices=USER_TYPE_CHOICES, default=Enums.REGULAR_USER.value)

    email = models.EmailField(unique=True)

    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

    gender = models.CharField(max_length=20, choices=GENDER_CHOICES, null=True, blank=True)
    dob = models.DateField(verbose_name=_("DOB"), max_length=256, null=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_email_verified = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['phone','first_name', 'last_name']

    def __str__(self):
        return str(self.email)