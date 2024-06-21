from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from django.conf.urls.static import static

from django.conf import settings


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
    path("api/", include("core_apps.game.urls"), name="api"),
    path("api/", include("core_apps.crawler.urls"), name="api"),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


admin.site.site_header = "Hamster Kombat API Admin"
admin.site.site_title = "Hamster Kombat API Admin Portal"
admin.site.index_title = "Welcome to Hamster Kombat API Portal"
