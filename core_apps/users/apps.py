from django.apps import AppConfig


class UsersConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "core_apps.users"

    def ready(self):
        # noinspection PyUnresolvedReferences
        from . import signals  # noqa: F401
