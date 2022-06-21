import collections
import hmac
import hashlib
import string
import random

from django.views.generic import TemplateView
from django.views.decorators.cache import never_cache
from django.http import HttpResponse, HttpResponseRedirect
from django.conf import settings

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Session, QrCode
from .serializers import QrSerializer
from .tasks import update_url



def check_string(data):
    secret = hashlib.sha256()
    secret.update(settings.TGBOT.encode('utf-8'))
    sorted_params = collections.OrderedDict(sorted(data.items()))
    param_hash = sorted_params.pop('hash')
    msg = "\n".join(["{}={}".format(k, v) for k, v in sorted_params.items()])

    if param_hash == hmac.new(secret.digest(), msg.encode('utf-8'), digestmod=hashlib.sha256).hexdigest():
        return True
    return False


class StartSession(APIView):
    def post(self, request):
        try:
            if check_string(request.data):
                user_id = request.data['id']
                old_sessions = Session.objects.filter(user_id=user_id)
                old_sessions.delete()
                sess_hash = ''.join(random.choice(string.ascii_lowercase + string.ascii_uppercase + string.digits) for i in range(32))
                s = Session(user_id=user_id, sess_hash=sess_hash)
                s.save()
                return Response({'success': True, 'hash': sess_hash})
            else:
                return Response({'success': False})
        except:
            return Response({'success': False})


class AllQrs(APIView):
    def get(self, request):
        try:
            sess_hash = request.query_params['hash']
            user_id = Session.objects.get(sess_hash=sess_hash).user_id
            qrs = QrCode.objects.filter(user_id=user_id)
            return Response({'success': True, 'qrs': QrSerializer(qrs, many=True).data})
        except:
            return Response({'success': False})


class ManageQr(APIView):
    def get(self, request):
        try:
            sess_hash = request.query_params['hash']
            session = Session.objects.get(sess_hash=sess_hash)
            qr_id = request.query_params['id']
            qr = QrCode.objects.get(pk=qr_id)
        except:
            return Response({'success': False})

        if (qr.user_id != session.user_id):
            return Response({'success': False})

        return Response({'success': True, 'qr': QrSerializer(qr).data})


    def post(self, request):
        try:
            sess_hash = request.data['hash']
            user_id = Session.objects.get(sess_hash=sess_hash).user_id
            url = request.data['url']
            edit_time = request.data['edit_time']
        except:
            return Response({'success': False})

        qr = QrCode(user_id=user_id, url=url, edit_time=edit_time, entries=0)

        try:
            name = request.data['name']
            qr.name = name
        except:
            pass

        qr.save()
        return Response({'success': True, 'qr': QrSerializer(qr).data})


    def put(self, request):
        try:
            sess_hash = request.data['hash']
            session = Session.objects.get(sess_hash=sess_hash)
            qr_id = request.data['id']
            qr = QrCode.objects.get(pk=qr_id)
            edit_time = request.data['edit_time']
        except:
            return Response({'success': False})

        if (qr.user_id != session.user_id):
            return Response({'success': False})

        qr.edit_time = edit_time

        for field in request.data:
            if field != 'hash' and field != 'id' and field != 'edit_time' and field != 'timer':
                try:
                    setattr(qr, field, request.data[field])
                except:
                    pass
        
        try:
            timer = request.data['timer']
            update_url.apply_async((qr.id, next_url_time), countdown=int(timer))
        except:
            pass

        qr.save()
        return Response({'success': True, 'qr': QrSerializer(qr).data})


    def delete(self, request):
        try:
            sess_hash = request.data['hash']
            session = Session.objects.get(sess_hash=sess_hash)
            qr_id = request.data['id']
            qr = QrCode.objects.get(pk=qr_id)
        except:
            return Response({'success': False})

        if (qr.user_id != session.user_id):
            return Response({'success': False})

        try:
            qr.image.delete(save=True)
            qr.delete()
            return Response({'success': True})
        except:
            return Response({'success': False})


def Redirect(request, qr_id):
    try:
        qr = QrCode.objects.get(pk=qr_id)
        qr.entries += 1
        qr.save()
        return HttpResponseRedirect('http://' + qr.url)
    except:
        return HttpResponse('Sorry, an error occuried')
