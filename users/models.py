from django.db import models
from django.shortcuts import reverse
from django.contrib.auth.models import AbstractUser, BaseUserManager
from ckeditor_uploader.fields import RichTextUploadingField


class UserManager(BaseUserManager):
    """Define a model manager for User model with no username field."""

    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """Create and save a User with the given email and password."""
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        """Create and save a regular User with the given email and password."""
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        """Create and save a SuperUser with the given email and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)


class User(AbstractUser):

    username = None
    email = models.EmailField(unique=True)

    avatar = models.ImageField(
        upload_to='avatars', blank=True, null=True, verbose_name='Аватар')
    phone = models.CharField(max_length=15, blank=True, verbose_name='Телефон')
    bio = RichTextUploadingField(
        config_name='mini', verbose_name='О себе', blank=True, null=True)
    birthday = models.DateField(
        null=True, blank=True, verbose_name='Дата рожденья')
    guide = models.BooleanField(default=False, verbose_name='Гид')

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def get_absolute_url(self):
        return reverse("users:profile", kwargs={"pk": self.pk})

    def __str__(self):
        return self.email
