from django.db.models import QuerySet, Prefetch
from core_apps.profiles.models import ProfileCard


def get_profile_cards(profile) -> QuerySet[ProfileCard]:

    return ProfileCard.objects.filter(profile=profile).select_related(
        "related_level", "card"
    )
