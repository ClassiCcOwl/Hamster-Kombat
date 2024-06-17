from django.db.models import QuerySet
from core_apps.game.models import Card, Level


def create_level(
    level: int, upgrade_cost: int, profit_per_hour: int, slug: str
) -> QuerySet[Level]:

    card = Card.objects.get(slug=slug)
    return Level.objects.create(
        level=level,
        upgrade_cost=upgrade_cost,
        profit_per_hour=profit_per_hour,
        card=card,
    )
