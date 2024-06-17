from django.db.models import QuerySet
from core_apps.game.models import Category


def get_all_categories() -> QuerySet[Category]:
    return Category.objects.prefetch_related('cards').all()
