from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models

from core.models import BaseModel

from .managers import UserCustomManager


class UserCustomModel(AbstractBaseUser, PermissionsMixin, BaseModel): # main
    class Meta:
        db_table = 'user'
        ordering = ('id',)

    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    objects = UserCustomManager()


class UserProfileModel(BaseModel): # submain
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)
    user = models.OneToOneField(UserCustomModel, on_delete=models.CASCADE, related_name='profile')
