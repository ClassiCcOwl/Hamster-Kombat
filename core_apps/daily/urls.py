from django.urls import path
from .apis.daily import DailyCombosApi

urlpatterns = [
    path("v1/combos/<str:date>/", DailyCombosApi.as_view(), name="daily_combos"),
]
