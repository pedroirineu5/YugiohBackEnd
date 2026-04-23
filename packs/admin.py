from django.contrib import admin

from packs.models import Packs

@admin.register(Packs)
class PacksAdmin(admin.ModelAdmin):
    list_display = ('package_name', 'url_photo', 'price')
