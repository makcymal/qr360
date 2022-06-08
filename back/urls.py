from django.contrib import admin
from django.urls import path, include

from .api.views import AppView, StartSession, ManageQrs, Redirect


# do not touch this fucking shit
urlpatterns = [
    path('', AppView),
    path('admin/', admin.site.urls),
    path('api/s', StartSession.as_view()),
    path('api/qr', ManageQrs.as_view()),
    path('redirect/<int:id>', Redirect),
]
