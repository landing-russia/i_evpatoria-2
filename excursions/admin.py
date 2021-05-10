from django.contrib import admin
from .models import Excursion, Photo


@admin.register(Excursion)
class ExcursionAdmin(admin.ModelAdmin):

    prepopulated_fields = {"slug": ("name",)}


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):

    pass
