# Generated by Django 3.2.2 on 2021-05-10 17:30

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
            name='Excursion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255, verbose_name='Название экскурсии')),
                ('slug', models.SlugField(max_length=255, unique=True)),
                ('description', models.TextField(blank=True, verbose_name='Описание')),
                ('extra', models.TextField(blank=True, verbose_name='Дополнительная информация')),
                ('location', models.CharField(blank=True, max_length=255, null=True, verbose_name='Локация')),
                ('duration', models.CharField(blank=True, max_length=255, null=True, verbose_name='Длительность')),
                ('start_time', models.TimeField(blank=True, null=True)),
                ('max_people_count', models.CharField(blank=True, max_length=255, null=True, verbose_name='Кол-во человек')),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True, verbose_name='Стоимость')),
                ('types', models.CharField(choices=[('group', 'Групповая'), ('individual', 'Индивидуальная')], default='individual', max_length=10, verbose_name='Тип')),
                ('is_published', models.BooleanField(default=True, verbose_name='Опубликовано')),
                ('guide', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='excursions', to=settings.AUTH_USER_MODEL, verbose_name='Гид')),
            ],
            options={
                'verbose_name': 'Экскурсию',
                'verbose_name_plural': 'Экскурсии',
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, verbose_name='Подпись фото')),
                ('image', models.ImageField(blank=True, null=True, upload_to='excursions_photos', verbose_name='Фото')),
                ('excursion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='photos', to='excursions.excursion', verbose_name='Фото')),
            ],
            options={
                'verbose_name': 'Фото',
                'verbose_name_plural': 'Фото',
            },
        ),
    ]