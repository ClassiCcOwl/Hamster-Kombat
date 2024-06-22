from django.contrib import admin
from .models import Category, Card, Level
from django.forms import IntegerField, NumberInput
from django.db import models

class LevelsInstanceInline(admin.TabularInline):
    model = Level
    formfield_overrides = {
         models.IntegerField: {'widget': NumberInput(attrs={'size':'3'})},
    }

class CardsInstanceInline(admin.TabularInline):
    model = Card


class CategoryAdmin(admin.ModelAdmin):
    list_display = [
        "pkid",
        "name",
        "updated_at",
    ]
    list_display_links = [
        "pkid",
        "name",
    ]
    list_filter = [
        "name",
    ]

    inlines = [CardsInstanceInline]


class CardAdmin(admin.ModelAdmin):
    list_display = [
        "pkid",
        "name",
        "slug",
        "category",
        "image",
    ]
    list_display_links = [
        "pkid",
        "name",
        "slug",
    ]
    list_filter = [
        "category",
        "name",
    ]

    search_fields = [
        "name",
    ]

    ordering = [
        "name",
    ]

    inlines = [LevelsInstanceInline]
    formfield_overrides = {
         models.IntegerField: {'widget': NumberInput(attrs={'size':'3'})},
    }

class LevelAdmin(admin.ModelAdmin):
    list_display = [
        "pkid",
        "card",
        "level",
        "upgrade_cost",
        "profit_per_hour",
        "coin_per_profit",
    ]
    list_display_links = [
        "pkid",
        "card",
        "level",
    ]
    list_filter = [
        "card",
    ]

    search_fields = [
        "card__name",
    ]
    ordering = [
        "card__name",
    ]
    formfield_overrides = {
         models.IntegerField: {'widget': NumberInput(attrs={'size':'3'})},
    }

admin.site.register(Category, CategoryAdmin)
admin.site.register(Card, CardAdmin)
admin.site.register(Level, LevelAdmin)
