from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .forms import UserChangeForm, UserCreationForm

from .models import User


class UserAdmin(BaseUserAdmin):
    ordering = ["username"]
    form = UserChangeForm
    add_form = UserCreationForm
    model = User

    list_display = [
        "pkid",
        "id",
        "username",
        "is_active",
        "is_staff",
    ]

    list_display_links = [
        "pkid",
        "id",
        "username",
    ]

    list_filter = [
        "username",
        "is_staff",
        "is_active",
    ]

    fieldsets = (
        (
            "Login Credentials",
            {
                "fields": (
                    "username",
                    "password",
                ),
            },
        ),
        (
            "Permissions and Groups",
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (
            "Important Dates",
            {
                "fields": (
                    "last_login",
                    "date_joined",
                ),
            },
        ),
    )

    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "username",
                    "password1",
                    "password2",
                ),
            },
        ),
    )
    search_fields = [
        "username",
    ]


admin.site.register(User, UserAdmin)
