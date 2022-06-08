from django.contrib import admin

from .models import Session, QrCode


admin.site.register(Session)
admin.site.register(QrCode)
