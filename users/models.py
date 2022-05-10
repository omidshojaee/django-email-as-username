from django.db import models
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.hashers import make_password
from django.utils.translation import gettext_lazy as _

# Create your models here.


class CustomUserManager(BaseUserManager):
    '''
    Custom user model manager to set email as the primary identifier for authentication.
    '''

    use_in_migrations: True

    def _create_user(
        self: 'CustomUserManager', email: str, password: str, **extra_fields: dict
    ) -> 'CustomUser':
        '''
        Create and save a User with given Email and Password.
        '''
        if not email:
            raise ValueError(_('The given Email must be set.'))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.password = make_password(password)
        user.save(using=self._db)
        return user

    def create_user(
        self: 'CustomUserManager', email: str, password: str, **extra_fields: dict
    ) -> 'CustomUser':
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(
        self: 'CustomUserManager', email: str, password: str, **extra_fields: dict
    ) -> 'CustomUser':
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))

        return self._create_user(email, password, **extra_fields)


class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(_('email address'), unique=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email
