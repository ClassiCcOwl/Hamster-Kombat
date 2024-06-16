from django.db.models import QuerySet
from core_apps.game.models import Category


def create_category(name: str) -> QuerySet[Category]:
    return Category.objects.create(name=name)
