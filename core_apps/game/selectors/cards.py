from django.db.models import QuerySet
from core_apps.game.models import Card


def get_all_categories_cards() -> QuerySet[Card]:
    return (
        Card.objects.only("name", "category", "slug").select_related("category").all()
    )


def get_single_category_cards(category: str) -> QuerySet[Card]:
    return (
        Card.objects.only("name", "category", "slug")
        .filter(category__name=category)
        .select_related("category")
    )


def get_single_card(slug: str) -> Card:
    return Card.objects.select_related("category").get(slug=slug)
