from django.contrib import admin

from packs.models import Pack


@admin.register(Pack)
class PackAdmin(admin.ModelAdmin):
    list_display = ("name", "cover_url", "price")
    filter_horizontal = ("cards",)
    search_fields = ("name", "description")
