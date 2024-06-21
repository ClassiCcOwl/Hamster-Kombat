from django.db import models
from core_apps.common.models import TimeStampedModel
from core_apps.game.models import Card
from django.utils import timezone


class DailyCombo(TimeStampedModel):
    combo_date = models.DateField(unique=True, default=timezone.now)
    card_no_1 = models.ForeignKey(Card, on_delete=models.PROTECT, related_name='cad1')
    card_no_2 = models.ForeignKey(Card, on_delete=models.PROTECT, related_name='cad2')
    card_no_3 = models.ForeignKey(Card, on_delete=models.PROTECT, related_name='cad3')

    class Meta:
        indexes = [
            models.Index(fields=["combo_date"]),
        ]

    def __str__(self) -> str:
        return f"{self.combo_date} {self.card_no_1.name} {self.card_no_2.name} {self.card_no_3.name}"
    
