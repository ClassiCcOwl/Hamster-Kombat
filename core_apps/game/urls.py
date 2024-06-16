from django.urls import path
from .apis.categories import CategoriesApi

urlpatterns = [
    path("categories/", CategoriesApi.as_view(), name="categories"),
]
