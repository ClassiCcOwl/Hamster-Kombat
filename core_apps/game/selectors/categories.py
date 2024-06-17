from django.db.models import QuerySet
from core_apps.game.models import Category, Card


def get_all_categories() -> QuerySet[Category]:
    return Category.objects.prefetch_related("cards").all()


def get_single_categories_cards(category) -> QuerySet[Card]:
    return Card.objects.filter(category__name=category).all()
