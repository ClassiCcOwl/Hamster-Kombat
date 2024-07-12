from django.urls import path
from .apis.profile import ProfileAPI
from .apis.profile_cards import ProfileCards, ProfileAddCard


urlpatterns = [
    path("v1/profile/", ProfileAPI.as_view(), name="profile"),
    path("v1/profile/mycards/", ProfileCards.as_view(), name="mycards"),
    path(
        "v1/profile/mycards/add/<uuid:card_id>/<int:level>/",
        ProfileAddCard.as_view(),
        name="add_profile_card",
    ),
]
