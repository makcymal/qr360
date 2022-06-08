from django.contrib import admin
from django.urls import path, include

from .api.views import AppView, StartSession, ManageQrs, Redirect


urlpatterns = [
    path('', AppView),
    path('admin', admin.site.urls),
    path('api/s', StartSession.as_view()),
    path('api/qr', StartSession.as_view()),
    path('redirect/<int:id>', Redirect),
]
