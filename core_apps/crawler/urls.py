from django.urls import path
from .api.crawler import LevelApi


urlpatterns = [
    path("v1/new_levels/", LevelApi.as_view(), name="new levels"),

]
