from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models

from core.models import BaseModel

from .managers import UserCustomManager


class UserCustomModel(AbstractBaseUser, PermissionsMixin, BaseModel):
    class Meta:
        db_table = 'user'
        ordering = ('id',)

    email = models.EmailField()
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    EMAIL_FIELD = 'email'
    objects = UserCustomManager()


class UserProfile(BaseModel):
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)
