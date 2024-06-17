from django.db.models import QuerySet
from core_apps.game.models import Card


def get_cards() -> QuerySet[Card]:
    return Card.objects.select_related("category").all() 


def get_card(category) -> QuerySet[Card]:
    return Card.objects.filter(category__name=category).select_related('category')
