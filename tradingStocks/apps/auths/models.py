from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin,
)
from django.utils import timezone
from django.db import models
from django.db.models import QuerySet
from django.contrib.auth.base_user import BaseUserManager
from django.core.exceptions import ValidationError

from abstracts.models import AbstractDateTime


class CustomUserManager(BaseUserManager): # создаем пользователя и сохраняем в БД 

    def create_user( # для создания простого пользователя
        self,
        user_name: str,
        first_name: str,
        last_name: str,
        email: str,
        image_url,
        password: str,
    ) -> 'CustomUser':

        if not email:
            raise ValidationError('Email required')
        
        if not image_url:
            raise ValidationError('Картинка где')

        user: 'CustomUser' = self.model(
            user_name=user_name,
            first_name=first_name,
            last_name=last_name,
            email=self.normalize_email(email),
            image_url=image_url,
            password=password,
        )
        user.set_password(password)
        user.save(using=self._db) # сохраняет в базе данных
        return user

    def create_superuser( # для создания главного пользователя
        self,
        user_name: str,
        first_name: str,
        last_name: str,
        email: str,
        password: str,
    ) -> 'CustomUser':

        user: 'CustomUser' = self.model(
            user_name=user_name,
            first_name=first_name,
            last_name=last_name,
            email=self.normalize_email(email),
            password=password,
        )
        user.is_staff = True
        user.is_superuser = True
        user.set_password(password)
        user.save(using=self._db)
        return user

    def get_not_deleted(self) -> QuerySet['CustomUser']:
        return self.filter(
            datetime_deleted__isnull=True
        )

    def get_deleted(self) -> QuerySet['CustomUser']:
        return self.filter(
            datetime_deleted__isnull=False
        )

class CustomUser(
    AbstractBaseUser,
    PermissionsMixin,
    AbstractDateTime # отражает дату создания
):
    user_name = models.CharField(max_length=150, unique=True, verbose_name='Имя пользователя')
    first_name = models.CharField(max_length=150, blank=True, verbose_name='Имя')
    last_name = models.CharField(max_length=150, blank=True, verbose_name='Фамилия')
    email = models.EmailField(
        'Почта/Логин', unique=True
    )

    def upload_to(instance, user_name):
        return 'images/{user_name}'.format(user_name=user_name)
    
    image_url = models.ImageField(upload_to=upload_to, blank=True, null=True, verbose_name='Фото пользователя')
    is_active = models.BooleanField(verbose_name='Активность', default=True)
    is_staff = models.BooleanField(verbose_name='Статус менеджера', default=False)
    date_joined = models.DateTimeField(
        verbose_name='Дата регистрации', default=timezone.now
    )
    USERNAME_FIELD = 'user_name'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'email'] #  еще что надо заполнить 

    objects = CustomUserManager()

    class Meta:
        ordering = (
            'date_joined',
        )
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'