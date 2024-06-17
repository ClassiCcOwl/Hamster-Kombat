from django.db import models
from core_apps.common.models import TimeStampedModel
from django.db.models import F


class Category(TimeStampedModel):

    name = models.CharField(max_length=30)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
        indexes = [
            models.Index(fields=['name']), 
        ]

    def __str__(self) -> str:
        return self.name


class Card(TimeStampedModel):
    name = models.CharField(max_length=50)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="cards"
    )
    image = models.ImageField(upload_to="card_images", blank=True)

    def __str__(self) -> str:
        return self.name

    class Meta:
        unique_together = [["name", "category"]]
        indexes = [
            models.Index(fields=['name']), 
            models.Index(fields=['category']), 
        ]


class Level(TimeStampedModel):
    level = models.IntegerField()
    upgrade_cost = models.PositiveIntegerField()
    profit_per_hour = models.PositiveIntegerField()
    card = models.ForeignKey(Card, on_delete=models.CASCADE, related_name="levels")
    coin_per_profit = models.PositiveIntegerField(blank=True, editable=False)

    class Meta:
        unique_together = [["level", "card"]]
        ordering = ["-level"]

    def __str__(self) -> str:
        return f"{self.card.name} Level {self.level}"

    def save(self, *args, **kwargs):
        self.coin_per_profit = self.upgrade_cost // self.profit_per_hour
        super(Level, self).save(*args, **kwargs)
