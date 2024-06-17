from django.urls import path
from .apis.categories import AllCategoriesApi
from .apis.cards import AllCategoriesCardsApi, SingleCategoryCardsApi, SingleCardApi

urlpatterns = [
    path("categories/", AllCategoriesApi.as_view(), name="categories"),
    path("cards/", AllCategoriesCardsApi.as_view(), name="all_categories_cards"),
    path(
        "cards/<str:category>/",
        SingleCategoryCardsApi.as_view(),
        name="single_category_cards",
    ),
    path("card/<str:slug>/", SingleCardApi.as_view(), name="single_card"),
]
