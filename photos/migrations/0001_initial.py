# Generated by Django 4.1.7 on 2023-04-22 06:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Favorite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name': ('Избранная запись',),
                'verbose_name_plural': 'Избранные записи',
            },
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('signature', models.CharField(max_length=100, verbose_name='Подпись')),
                ('photo', models.ImageField(blank=True, upload_to='photos', verbose_name='Фото')),
                ('is_deleted', models.BooleanField(default=False, verbose_name='Удалено')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата и время создания')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Дата и время обновления')),
                ('deleted_at', models.DateTimeField(default=None, null=True, verbose_name='Дата и время удаления')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='photos_Photo', to=settings.AUTH_USER_MODEL, verbose_name='Автор')),
                ('favorite', models.ManyToManyField(related_name='photos', through='photos.Favorite', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Фото',
                'verbose_name_plural': 'Фотографии',
            },
        ),
        migrations.AddField(
            model_name='favorite',
            name='photo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='favorite_users', to='photos.photo', verbose_name='Избранное'),
        ),
        migrations.AddField(
            model_name='favorite',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='favorite_photos', to=settings.AUTH_USER_MODEL, verbose_name='Избранное'),
        ),
    ]
