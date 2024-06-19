from django.urls import path
from .apis.categories import AllCategoriesApi, SingleCategoryCardsApi
from .apis.cards import AllCardsApi, SingleCardApi
from .apis.levels import LevelApi


urlpatterns = [
    path("v1/categories/", AllCategoriesApi.as_view(), name="all_categories"),
    path(
        "v1/categories/<str:category>",
        SingleCategoryCardsApi.as_view(),
        name="single_category_cards",
    ),
    path("v1/cards/", AllCardsApi.as_view(), name="all_cards"),
    path("v1/cards/<str:slug>/", SingleCardApi.as_view(), name="single_card"),
    path("v1/cards/<str:slug>/levels/", LevelApi.as_view(), name="card_levels"),
]
