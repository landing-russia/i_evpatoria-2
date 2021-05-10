from django.contrib import admin
from django.db import models
from django.contrib.auth.admin import UserAdmin
from .models import User


@admin.register(User)
class CustomUserAdmin(UserAdmin):

    fieldsets = UserAdmin.fieldsets + (
        (
            'Профиль',
            {
                'fields': (
                    'avatar',
                    'phone',
                    'bio',
                    'birthday',
                    'guide',
                )
            }
        ),
    )
