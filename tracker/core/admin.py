from django.contrib import admin

from .models import Sighting

# Register your models here.
@admin.register(Sighting)
class SightingAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Sighting._meta.get_fields()]