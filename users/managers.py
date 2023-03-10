from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _


class CustomUserManager(BaseUserManager):
    def create_user(self, username, email, password, name, city, **extra_fields):
        if not email:
            raise ValueError(_('Почта обязательна для регистрации'))
        email = self.normalize_email(email)
        user = self.model(email=email, name=name, city=city, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, name, city, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Для суперпользователя is_staff должно быть True'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Для суперпользователя is_superuser должно быть True'))
        
        return self.create_user(email, password, name, city, **extra_fields)