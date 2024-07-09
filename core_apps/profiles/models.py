from django.db import models
from django.forms import ValidationError
from core_apps.users.models import User
from core_apps.game.models import Card, Level
from core_apps.common.models import TimeStampedModel


class Profile(TimeStampedModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50, null=True, blank=True)
    last_name = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self) -> str:
        return f"{self.user}"

    class Meta:
        indexes = [
            models.Index(fields=["user"]),
        ]


class ProfileCard(TimeStampedModel):
    profile = models.ForeignKey(
        Profile, on_delete=models.CASCADE, related_name="profile_cards"
    )
    card = models.ForeignKey(
        Card, on_delete=models.PROTECT, related_name="profile_cards"
    )

    level = models.PositiveSmallIntegerField(default=1)

    related_level = models.ForeignKey(
        Level, on_delete=models.PROTECT, null=True, blank=True, editable=False
    )

    def __str__(self):
        return f"{self.profile}"

    class Meta:
        unique_together = ("profile", "card")
        indexes = [
            models.Index(fields=["profile"]),
        ]

    def save(self, *args, **kwargs):

        if self.level is not None:
            related_instance = Level.objects.filter(card=self.card, level=self.level)
            if related_instance.exists():
                self.related_level = related_instance.first()

        super().save(*args, **kwargs)
