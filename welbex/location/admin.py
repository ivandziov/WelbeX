from django.contrib import admin

from cargo.models import Location


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    pass
