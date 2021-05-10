from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):

    avatar = models.ImageField(
        upload_to='avatars', blank=True, null=True, verbose_name='Аватар')
    phone = models.CharField(max_length=15, blank=True, verbose_name='Телефон')
    bio = models.TextField(blank=True, verbose_name='О себе')
    birthday = models.DateField(
        null=True, blank=True, verbose_name='Дата рожденья')
    guide = models.BooleanField(default=False, verbose_name='Гид')
