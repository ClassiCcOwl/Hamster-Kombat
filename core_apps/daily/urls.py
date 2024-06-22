from django.urls import path
from .apis.daily import DailyCombosApi, TodayCombosApi

urlpatterns = [
    path("v1/combos/today/", TodayCombosApi.as_view(), name="daily_combos"),
    path("v1/combos/<str:date>/", DailyCombosApi.as_view(), name="daily_combos"),
]
