from django.contrib import admin
from music import models

# Register your models here.
@admin.register(models.Music)
class MusicAdmin(admin.ModelAdmin):
    fields = ['name', 'image', 'file', 'duration', 'is_active']
    