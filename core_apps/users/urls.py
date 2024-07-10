from django.urls import path
from .views import CustomUserDetailsView


urlpatterns = [
    path("v1/auth/user/", CustomUserDetailsView.as_view(), name="user_details"),
]
