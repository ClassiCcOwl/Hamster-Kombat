from django.db.models import QuerySet
from core_apps.game.models import Card
from core_apps.game.models import Category


def get_cards() -> QuerySet[Card]:
    return Card.objects.all()


def get_card(category) -> QuerySet[Card]:
    return Card.objects.filter(category__name=category)
