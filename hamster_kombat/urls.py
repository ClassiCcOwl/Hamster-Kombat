from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from django.conf.urls.static import static

from django.conf import settings
from dj_rest_auth.views import PasswordResetConfirmView
import os

schema_view = get_schema_view(
    openapi.Info(
        title="Hamster Kombat API",
        default_version="V1",
        description="API endpoints for hamster kombat",
        contact=openapi.Contact(email="khavari.7878@yahoo.com"),
        license=openapi.License(name="MIT Licence"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path("", schema_view.with_ui("swagger", cache_timeout=0)),
    path("admin/", admin.site.urls),
    path("api/", include("core_apps.game.urls"), name="api_game"),
    path("api/", include("core_apps.crawler.urls"), name="api_crawler"),
    path("api/", include("core_apps.daily.urls"), name="api_daily"),
    path("api/", include("core_apps.profiles.urls"), name="api_profile"),
    path("api/", include("core_apps.users.urls")),
    path("api/v1/auth/", include("dj_rest_auth.urls")),
    path("api/v1/auth/registration/", include("dj_rest_auth.registration.urls")),
    path(
        "api/v1/auth/password/reset/confirm/<uidb64>/<token>/",
        PasswordResetConfirmView.as_view(),
        name="password_reset_confirm",
    ),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


environ_mode = os.environ.get("DJANGO_ENVIRON_MODE", "local")


if environ_mode == "local":
    from debug_toolbar.toolbar import debug_toolbar_urls

    urlpatterns = [
        *urlpatterns,
    ] + debug_toolbar_urls()


admin.site.site_header = "Hamster Kombat API Admin"
admin.site.site_title = "Hamster Kombat API Admin Portal"
admin.site.index_title = "Welcome to Hamster Kombat API Portal"
