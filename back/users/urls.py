from django.urls import include, path

from . import views

urlpatterns = [
    path('', include('rest_registration.api.urls')),
    path('telegram-auth/', views.TelegramAuth.as_view()),
]
