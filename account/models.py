from django.db import models
from .managers import UserManager
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.db import models



# ==============================Custom User==================================
class Custom_User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=30, unique=True, validators=[UnicodeUsernameValidator])
    email = models.EmailField(max_length=40, unique=True)

    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    
    
    date_joined = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']
    
    class Meta:
        ordering = ['-date_joined']
    
    def __str__(self) -> str:
        return self.username







