from django.db.models import QuerySet
from core_apps.game.models import Level


def get_levels(slug: str) -> QuerySet[Level]:
    return Level.objects.filter(card__slug=slug).all()
