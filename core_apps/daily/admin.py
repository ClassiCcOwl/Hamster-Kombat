from django.contrib import admin
from .models import DailyCombo

# Register your models here.
class DailyComboAdmin(admin.ModelAdmin):
    list_display = [
        "combo_date",
        "card_no_1",
        "card_no_2",
        "card_no_3",
    ]
    list_display_links = [
        "combo_date",
    ]
    list_filter = [
        "combo_date",
    ]


admin.site.register(DailyCombo, DailyComboAdmin)