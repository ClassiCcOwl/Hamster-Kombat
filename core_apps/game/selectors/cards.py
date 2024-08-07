from django.db.models import QuerySet, Prefetch
from core_apps.game.models import Card, Level


def get_all_cards() -> QuerySet[Card]:

    query = (
        Card.objects.only(
            "id",
            "name",
            "category",
            "slug",
            "image",
        )
        .prefetch_related(
            Prefetch("levels__card"),
        )
        .select_related("category")
        .all()
        # .prefetch_related(
        #     "levels",
        # )
    )
    return query


def get_single_card(slug: str) -> Card:
    return (
        Card.objects.prefetch_related("levels")
        .select_related("category")
        .get(slug=slug)
    )


def get_recently_added_cards(n: int) -> QuerySet[Card]:

    return Card.objects.all().order_by("-created_at")[:n]


def get_single_card_by_id(card_id):
    return Card.objects.get(id=card_id)
