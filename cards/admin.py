from django.contrib import admin

class CardsAdmin(admin.ModelAdmin):
    list_display = ('name','rarity','card_type')