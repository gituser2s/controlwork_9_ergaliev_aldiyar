from django.contrib.auth.models import AbstractUser
from django.db import models
from accounts.managers import UserManager


class Account(AbstractUser):
    username = models.CharField(verbose_name="Логин", unique=True, null=False, max_length=50)
    email = models.EmailField(verbose_name='Электронная почта', unique=True, blank=True)
    avatar = models.ImageField(
        upload_to='user_pic',
        verbose_name='Аватар',
    )
    gender = models.CharField(
        max_length=50,
        choices=(('Мужской', 'Мужской'), ('Женский', 'Женский'))
    )

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    object = UserManager()

    class Meta:
        verbose_name = 'Аккаунт'
        verbose_name_plural = 'Аккаунт'
