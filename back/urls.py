from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from .api.views import AppView, StartSession, ManageQr, AllQrs, Redirect


urlpatterns = [
    path('', AppView),
    path('admin/', admin.site.urls),
    path('api/s', StartSession.as_view()),
    path('api/qr', ManageQr.as_view()),
    path('api/qrs', AllQrs.as_view()),
    path('redirect/<int:qr_id>', Redirect),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
