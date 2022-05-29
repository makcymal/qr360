from django.urls import path, include, re_path

from .views import *


urlpatterns = [
	path('auth/', include ('djoser.urls')),
	re_path(r'^auth/', include ('djoser.urls.authtoken')),
]