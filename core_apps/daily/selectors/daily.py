from datetime import datetime
from core_apps.daily.models import DailyCombo
from django.db.models import QuerySet


def get_daily_combo(date: str, format: str = "%Y-%m-%d") -> QuerySet[DailyCombo]:

    date = datetime.strptime(date, format).date()

    combos = DailyCombo.objects.select_related(
        "card_no_1",
        "card_no_2",
        "card_no_3",
        "card_no_1__category",
        "card_no_2__category",
        "card_no_3__category",
    ).get(combo_date=date)

    return combos


def get_today_daily_combo() -> QuerySet[DailyCombo]:
    combos = DailyCombo.objects.select_related(
        "card_no_1",
        "card_no_2",
        "card_no_3",
        "card_no_1__category",
        "card_no_2__category",
        "card_no_3__category",
    ).latest("combo_date")

    return combos
