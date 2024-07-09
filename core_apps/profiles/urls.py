from django.urls import path
from .apis.profile import Profile
from .apis.profile_cards import ProfileCards


urlpatterns = [
    path("v1/profile/", Profile.as_view(), name="profile"),
    path("v1/profile/mycards/", ProfileCards.as_view(), name="profile"),
]
