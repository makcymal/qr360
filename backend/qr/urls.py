from django.urls import path, include

from .views import StartSession, ManageQrs, AppView, Redirect


urlpatterns = [
    path('api/s', StartSession.as_view()),
    path('api/qr', ManageQrs.as_view()),
    path('redirect/<int:id>/', Redirect),
    path('', AppView),
    path('<path:vue>/', AppView)
]