from django.urls import path
from .apis.categories import AllCategoriesApi, SingleCategoryCardsApi

from .apis.cards import AllCardsApi, SingleCardApi

urlpatterns = [
    path("categories/", AllCategoriesApi.as_view(), name="all_categories"),
    path(
        "categories/<str:category>",
        SingleCategoryCardsApi.as_view(),
        name="single_category_cards",
    ),
    path("cards/", AllCardsApi.as_view(), name="all_categories_cards"),
    path("cards/<str:slug>/", SingleCardApi.as_view(), name="single_card"),
]
