from django.db.models import QuerySet
from core_apps.game.models import Category


def get_categories() -> QuerySet[Category]:
    return Category.objects.all()
