from typing import Iterable
from django.db import models
from .managers import UserManager
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.contrib.auth.tokens import default_token_generator
from django.dispatch import receiver
from django.db.models.signals import post_save

class Custom_User(AbstractBaseUser, PermissionsMixin):
    USER_TYPE = (
        ('Admin', 'Admin'),
        ('Sub-Admin', 'Sub-Admin'),
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



class User_Authentication_Model(models.Model):
    user = models.OneToOneField(Custom_User, on_delete=models.CASCADE, related_name='user_authentication')
    login_url = models.URLField(blank=True, null=True)
    
    def save(self, *args, **kwargs):
        token = default_token_generator.make_token(self.user)
        self.login_url = f'http://127.0.0.1:8000/login/{token}/'
        super(User_Authentication_Model, self).save(*args, **kwargs)
    
    def __str__(self) -> str:
        return f'{self.user} - {self.login_url}'




@receiver(post_save, sender=Custom_User)
def create_user_authentication_model(sender, instance, created, **kwargs):
    if created:
        User_Authentication_Model.objects.create(user=instance)

