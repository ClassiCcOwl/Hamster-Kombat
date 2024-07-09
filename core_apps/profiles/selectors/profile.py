from django.db.models import QuerySet, Prefetch
from core_apps.profiles.models import Profile


def get_profile(user) -> Profile:
    return Profile.objects.get(user=user)
