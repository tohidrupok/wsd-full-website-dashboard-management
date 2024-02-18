from django.contrib.auth.base_user import BaseUserManager

class UserManager(BaseUserManager):
    def create_user(self, name, username, email, password, **extra_field):
        if not username:
            raise ValueError('Username must be set!')
        if not email:
            raise ValueError('Email must be set!')
        user = self.model(
            name=name, username = username, email = email, **extra_field
        )
        user.set_password(password)
        user.save(using = self._db)
        return user

    def create_superuser(self, name, username, email, password, **extra_field):
        user = self.create_user(
            name=name, username = username, password=password, email = email, **extra_field
        )
        user.is_staff = True
        user.is_superuser = True
        user.is_active = True
        user.user_type = 'Admin'
        user.save(using=self._db)
        return user
    