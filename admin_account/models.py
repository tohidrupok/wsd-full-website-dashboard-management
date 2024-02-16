from typing import Iterable
from django.db import models
from .managers import UserManager
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.validators import UnicodeUsernameValidator

class Custom_User(AbstractBaseUser, PermissionsMixin):
    USER_TYPE = (
        ('Admin', 'Admin'),
        ('Sub-Admin', 'Sub-Admin'),
        ('Staff', 'Staff'),
        ('Invantory', 'Invantory'),
        ('RTS', 'RTS'),
    )
    name = models.CharField(max_length=100, blank=True, null=True)
    username = models.CharField(max_length=30, unique=True, validators=[UnicodeUsernameValidator])
    email = models.EmailField(max_length=40, unique=True)
    user_type = models.CharField(choices=USER_TYPE, blank=True, null=True, max_length=50)

    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    
    date_joined = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'name']
    
    class Meta:
        ordering = ['-date_joined']
    
    def __str__(self) -> str:
        return self.username
    

    

