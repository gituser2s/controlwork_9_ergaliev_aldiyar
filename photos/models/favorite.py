from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from accounts.models import Account
from django.db import models
from photos.models.photo import Photo


class Favorite(models.Model):
    user = models.ForeignKey(
        to=Account,
        related_name='favorite_photos',
        verbose_name='Избранное',
        null=False,
        on_delete=models.CASCADE
    )
    photo = models.ForeignKey(
        to=Photo,
        related_name='favorite_users',
        verbose_name='Избранное',
        null=False,
        on_delete=models.CASCADE
    )
    note = models.CharField(
        max_length=30,
        verbose_name='Текстовая заметка',
        null=False,
        blank=True
    )

    class Meta:
        verbose_name = 'Избранная запись',
        verbose_name_plural = 'Избранные записи'