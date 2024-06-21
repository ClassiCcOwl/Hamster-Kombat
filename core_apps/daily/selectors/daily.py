from datetime import datetime
from core_apps.daily.models import DailyCombo


def get_daily_combo(date, format="%Y-%m-%d"):

    date = datetime.strptime(date, format).date()

    combos = DailyCombo.objects.select_related(
        "card_no_1", "card_no_2", "card_no_3", "card_no_1__category", "card_no_2__category", "card_no_3__category"
    ).get(combo_date=date)

    return combos
