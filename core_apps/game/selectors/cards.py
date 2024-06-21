from django.db.models import QuerySet, Prefetch
from core_apps.game.models import Card, Level


def get_all_cards() -> QuerySet[Card]:

    query = (
        Card.objects.only(
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
