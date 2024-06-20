from django.db.models import QuerySet
from core_apps.game.models import Card


def get_all_cards() -> QuerySet[Card]:
    return (
        Card.objects.only("id", "name", "category", "slug", "updated_at", "image")
        .select_related("category")
        .all()
    )


def get_single_card(slug: str) -> Card:
    return (
        Card.objects.prefetch_related("levels")
        .select_related("category")
        .get(slug=slug)
    )
