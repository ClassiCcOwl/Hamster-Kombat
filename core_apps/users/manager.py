from django.contrib.auth.base_user import BaseUserManager
from django.core.exceptions import ValidationError


class CustomUserManeger(BaseUserManager):
    def create_user(self, first_name, last_name, username, password, **extra_fields):
        if not first_name:
            raise ValueError("User must have a first name.")

        if not last_name:
            raise ValueError("User must have a last name.")
        if not username:
            raise ValueError("User must have a username.")

        user = self.model(
            first_name=first_name,
            last_name=last_name,
            username=username,
            **extra_fields
        )
        user.set_password(password)
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)

        user.save(using=self._db)
        return user

    def create_superuser(
        self, first_name, last_name, username, password, **extra_fields
    ):

        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if not extra_fields.get("is_staff"):
            raise ValueError("Superuser must have is_staff=True.")
        if not extra_fields.get("is_superuser"):
            raise ValueError("Superuser must have is_superuser=True.")
        if not password:
            raise ValueError("Superuser must have a password.")
        if not username:
            raise ValueError("Superuser must have a username.")

        user = self.create_user(
            first_name, last_name, username, password, **extra_fields
        )
        user.save(using=self._db)
        return user
