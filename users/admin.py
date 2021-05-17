from django.contrib import admin
from django.db import models
from django.contrib.auth.admin import UserAdmin
from .models import User


@admin.register(User)
class CustomUserAdmin(UserAdmin):

    list_display = ('email', 'first_name', 'last_name', 'is_active', 'is_staff')

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

    ordering = ('email',)
