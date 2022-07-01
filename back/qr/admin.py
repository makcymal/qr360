from django.contrib import admin

from .models import DemoQR, QRModel


admin.site.register(QRModel)
admin.site.register(DemoQR)
