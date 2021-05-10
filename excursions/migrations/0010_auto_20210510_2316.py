# Generated by Django 3.2.2 on 2021-05-10 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('excursions', '0009_auto_20210510_2237'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='photo',
            name='image_small',
        ),
        migrations.AlterField(
            model_name='photo',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='excursions_photos', verbose_name='Фото'),
        ),
        migrations.AlterField(
            model_name='photo',
            name='name',
            field=models.CharField(default='Фото', max_length=100, verbose_name='Подпись фото'),
        ),
    ]
