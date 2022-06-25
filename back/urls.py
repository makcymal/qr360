from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView
from django.views.decorators.cache import never_cache
from django.http import HttpResponse, HttpResponseRedirect
from django.db.models import F

from qr.models import QRModel

AppView = never_cache(TemplateView.as_view(template_name='index.html'))


def Redirect(request, qr_id):
    try:
        qr = QRModel.objects.get(pk=qr_id)
        qr.entries = F('entries') + 1
        qr.save()
        return HttpResponseRedirect('http://' + qr.url)
    except:
        return HttpResponse('Sorry, an error occuried')


urlpatterns = [
    path('', AppView, name='app'),
    path('profile/',
         TemplateView.as_view(template_name='profile.html'),
         name='profile'),
    path('admin/', admin.site.urls),
    path('redirect/<int:qr_id>', Redirect),
    path('api/', include('api.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
