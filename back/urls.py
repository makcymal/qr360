from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.http import HttpResponse, HttpResponseRedirect
from django.db.models import F

from qr.models import QRModel, DemoQR


def Redirect(request, qr_id):
    try:
        qr = QRModel.objects.get(pk=qr_id)
        qr.entries = F('entries') + 1
        qr.save()
        return HttpResponseRedirect('http://' + qr.url)
    except:
        return HttpResponse('Sorry, an error occuried')


def DemoRedirect(request, qr_id):
    try:
        qr = DemoQR.objects.get(pk=qr_id)
        return HttpResponseRedirect('http://' + qr.url)
    except:
        return HttpResponse('Sorry, an error occuried')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('redirect/<int:qr_id>/', Redirect),
    path('demo-redirect/<int:qr_id>/', DemoRedirect),
    path('api/', include('api.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
