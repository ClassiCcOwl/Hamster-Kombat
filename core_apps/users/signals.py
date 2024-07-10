from django.db.models.signals import post_save
from django.dispatch import receiver
from core_apps.users.models import User
from ..profiles.models import Profile


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    print('new user singal')
    if created:
        Profile.objects.create(user=instance)