from django import forms
from django.contrib import admin
from django.forms.models import BaseInlineFormSet
from core_apps.game.models import Level
from .models import Profile, ProfileCard


class ProfileCardInstanceInline(admin.TabularInline):
    model = ProfileCard


class ProfileAdmin(admin.ModelAdmin):
    list_display = ["pkid", "user", "first_name", "last_name"]
    list_display_links = ["pkid", "user"]
    list_filter = ["user"]
    search_fields = ["user"]
    inlines = [ProfileCardInstanceInline]


class ProfileCardAdmin(admin.ModelAdmin):
    list_display = ["pkid", "profile", "card", "level"]
    list_display_links = ["pkid", "card"]
    list_filter = ["profile", "card"]
    search_fields = ["profile", "card"]


admin.site.register(Profile, ProfileAdmin)
admin.site.register(ProfileCard, ProfileCardAdmin)
