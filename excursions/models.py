from datetime import datetime
from django.db import models
from django.core.exceptions import ValidationError
from PIL import Image
from i_evpatoria.models import TimeStampedModel


def excursions_photos_path(instance, filename):
    return 'excursions_photos/{0}/{1}/{2}/{3}'.format(datetime.now().year, datetime.now().month, instance.excursion.slug, filename)


class Photo(models.Model):
    def validate_image(fieldfile_obj):
        filesize = fieldfile_obj.file.size
        megabyte_limit = 5
        if filesize > megabyte_limit*1024*1024:
            raise ValidationError(
                "Максимальный размер файла %s MB" % str(megabyte_limit))

    name = models.CharField(max_length=100, default='Фото',
                            verbose_name='Подпись фото')
    excursion = models.ForeignKey(
        'Excursion', on_delete=models.CASCADE, related_name='photos', verbose_name='Экскурсия')
    image = models.ImageField(
        upload_to=excursions_photos_path, max_length=300, validators=[validate_image], verbose_name='Фото', null=True, blank=True)

    def __str__(self):
        return self.excursion.name

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        SIZE = 1920, 1400

        if self.image:
            pic = Image.open(self.image.path)
            if  pic.width > 1920 or pic.height > 1400:
                pic.thumbnail(SIZE, Image.LANCZOS)
                pic.save(self.image.path)

    class Meta:
        verbose_name = 'Фото'
        verbose_name_plural = 'Фото'


class Excursion(TimeStampedModel):
    TYPES = (
        ('group', 'Групповая'),
        ('individual', 'Индивидуальная'),
    )
    guide = models.ForeignKey(
        'users.User', on_delete=models.CASCADE, related_name='excursions', verbose_name='Гид')
    name = models.CharField(max_length=255, verbose_name='Название экскурсии')
    slug = models.SlugField(max_length=255, unique=True)
    description = models.TextField(blank=True, verbose_name='Описание')
    extra = models.TextField(
        blank=True, verbose_name='Дополнительная информация')
    location = models.CharField(
        max_length=255, verbose_name='Локация', null=True, blank=True)
    duration = models.CharField(
        max_length=255, verbose_name='Длительность', null=True, blank=True)
    start_time = models.TimeField(
        blank=True, null=True, verbose_name='Время начала экскурсии')
    max_people_count = models.PositiveSmallIntegerField(
        verbose_name='Кол-во человек', null=True, blank=True)
    price = models.DecimalField(
        max_digits=7, decimal_places=2, verbose_name='Стоимость', null=True, blank=True)
    types = models.CharField(max_length=10, choices=TYPES,
                             verbose_name='Тип', default='individual')
    is_published = models.BooleanField(
        default=True, verbose_name='Опубликовано')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Экскурсию'
        verbose_name_plural = 'Экскурсии'
        ordering = ['-created']
