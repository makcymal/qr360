from django.urls import path, include

from .views import StartSession, ManageQrs


urlpatterns = [
    path('api/s', StartSession.as_view()),
    path('api/qrs', ManageQrs.as_view()),
]