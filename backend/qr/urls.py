from django.urls import path, include

from .views import StartSession, ManageQrs, AppView, Redirect, TestApi


urlpatterns = [
    path('api/s', StartSession.as_view()),
    path('api/qr', ManageQrs.as_view()),
    path('api/test', TestApi.as_view()),
    path('redirect/<int:id>/', Redirect),
    path('', AppView),
]