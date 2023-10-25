"""
    Create user models
"""

from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)


class UserManager(BaseUserManager):
    """Manager for users"""

    def create_user(self, email, mobile, password=None, **extra_fields):
        """Create, save and return a new user."""

        if not email:
            raise ValueError('User must have an email address.')

        if not mobile:
            raise ValueError('User must have a mobile number.')

        user = self.model(
            email=self.normalize_email(email),
            mobile=mobile,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, mobile, password=None):
        """Create and return new super user."""
        user = self.create_user(
            email, mobile, password,
            is_staff=True,
            is_superuser=True

        )
        user.save(using=self._db)
        return user



class User(AbstractBaseUser, PermissionsMixin):
    """
    Model for all users in the project. including,
    customer, seller/vendor, admin.
    """

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True)
    mobile = models.CharField(max_length=15, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)


    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['mobile']

    def __str__(self):
        return f"{self.email}"



class UserProfile(models.Model):
    """
    User profile model.
    """

    user = models.OneToOneField(
        User,
        related_name='userprofile',
        on_delete=models.CASCADE
    )
    resume = models.FileField(upload_to = 'uploads/resume/', null=True)
