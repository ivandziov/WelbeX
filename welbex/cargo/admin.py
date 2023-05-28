from django.contrib import admin

from cargo.models import Cargo


@admin.register(Cargo)
class CargoAdmin(admin.ModelAdmin):
    pass
