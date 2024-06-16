from django.db.models import QuerySet
from core_apps.game.models import Card, Category


def create_card(category: str, name: str, image: str) -> QuerySet[Card]:
    selected_category = Category.objects.get(name=category)
    return Card.objects.create(name=name, category=selected_category, image=image)
