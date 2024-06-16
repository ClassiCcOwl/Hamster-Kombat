from django.urls import path
from .apis.categories import CategoriesApi
from .apis.cards import CardsApi, CardApi

urlpatterns = [
    path("categories/", CategoriesApi.as_view(), name="categories"),
    path("cards/", CardsApi.as_view(), name="cards"),
    path("cards/<str:category>/", CardApi.as_view(), name="cards"),
]
