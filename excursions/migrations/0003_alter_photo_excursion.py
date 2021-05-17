# Generated by Django 3.2.3 on 2021-05-17 20:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('excursions', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='excursion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='photos', to='excursions.excursion', verbose_name='Экскурсия'),
        ),
    ]
