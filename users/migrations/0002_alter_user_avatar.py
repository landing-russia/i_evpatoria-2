# Generated by Django 3.2.3 on 2021-06-04 09:10

from django.db import migrations, models
import users.models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=models.ImageField(blank=True, max_length=300, null=True, upload_to='avatars', validators=[users.models.User.validate_image], verbose_name='Аватар'),
        ),
    ]
