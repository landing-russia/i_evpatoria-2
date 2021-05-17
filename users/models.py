from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from ckeditor_uploader.fields import RichTextUploadingField



class UserManager(BaseUserManager):
    def create_user(self, email, password=None):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_staffuser(self, email, password):
        """
        Creates and saves a staff user with the given email and password.
        """
        user = self.create_user(
            email,
            password=password,
        )
        user.is_staff = True
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        """
        Creates and saves a superuser with the given email and password.
        """
        user = self.create_user(
            email,
            password=password,
        )
        user.is_staff = True
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractUser):

    username = None
    email = models.EmailField(unique=True)

    avatar = models.ImageField(
        upload_to='avatars', blank=True, null=True, verbose_name='Аватар')
    phone = models.CharField(max_length=15, blank=True, verbose_name='Телефон')
    bio = RichTextUploadingField(config_name='mini', verbose_name='О себе', blank=True, null=True)
    birthday = models.DateField(
        null=True, blank=True, verbose_name='Дата рожденья')
    guide = models.BooleanField(default=False, verbose_name='Гид')

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

