from django.urls import path, include

from .views import Recaptcha

urlpatterns = [
    path('recaptcha/', Recaptcha.as_view()),
    path('qrs/', include('qr.urls')),
    path('users/', include('users.urls')),
]
