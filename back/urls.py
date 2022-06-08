from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from .api.views import AppView, StartSession, ManageQrs, Redirect


urlpatterns = [
    path('', AppView),
    path('admin/', admin.site.urls),
    path('api/s', StartSession.as_view()),
    path('api/qr', ManageQrs.as_view()),
    path('redirect/<int:id>', Redirect),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
