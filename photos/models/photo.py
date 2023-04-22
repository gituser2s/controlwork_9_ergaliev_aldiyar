from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone


class Photo(models.Model):
    signature = models.CharField(verbose_name="Подпись", null=False, blank=False, max_length=100)
    photo = models.ImageField(verbose_name='Фото', null=False, blank=True, upload_to='photos')
    author = models.ForeignKey(verbose_name='Автор', to=get_user_model(), related_name='photos_Photo', null=False,
                               blank=False,
                               on_delete=models.CASCADE)
    is_deleted = models.BooleanField(
        verbose_name='Удалено',
        null=False,
        default=False
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата и время создания"
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="Дата и время обновления"
    )
    deleted_at = models.DateTimeField(
        verbose_name='Дата и время удаления',
        null=True,
        default=None
    )
    favorite = models.ManyToManyField(
        through='photos.favorite',
        to=get_user_model(),
        related_name='photos'
    )

    def __str__(self):
        return f"{self.author} - {self.signature}"

    def delete(self, using=None, keep_parents=False):
        self.is_deleted = True
        self.deleted_at = timezone.now()
        self.save()

    class Meta:
        verbose_name = 'Фото'
        verbose_name_plural = 'Фотографии'
