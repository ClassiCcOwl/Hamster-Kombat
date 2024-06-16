from django.contrib import admin
from .models import Category, Card, Level


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


class CardAdmin(admin.ModelAdmin):
    list_display = [
        "pkid",
        "name",
        "category",
        "updated_at",
    ]
    list_display_links = [
        "pkid",
        "name",
    ]
    list_filter = [
        "name",
        "category",
    ]


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
        "level",
    ]
    list_filter = [
        "card",
    ]


admin.site.register(Category, CategoryAdmin)
admin.site.register(Card, CardAdmin)
admin.site.register(Level, LevelAdmin)
