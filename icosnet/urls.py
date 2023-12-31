from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("icosnet/", include("core.urls")),
    path("icosnet/", include("comptes.urls")),
    path("admin/", admin.site.urls),
    path("icosnet/", include("achat.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
