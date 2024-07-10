from ..models import ProfileCard


def create_or_update_profile_card(profile, card, level: int):
    profile_card, created = ProfileCard.objects.update_or_create(
        card=card,
        profile=profile,
        defaults={
            "level": level,
        },
    )
    profile_card.save()

    return profile_card
