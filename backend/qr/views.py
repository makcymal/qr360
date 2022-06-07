import collections
import hmac
import hashlib
import string
import random

from django.http import HttpResponse, HttpResponseRedirect
from django.conf import settings
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Session, QrCode
from .serializers import QrSerializer


# работает
def check_string(data):
    secret = hashlib.sha256()
    secret.update(settings.TGBOT.encode('utf-8'))
    sorted_params = collections.OrderedDict(sorted(data.items()))
    param_hash = sorted_params.pop('hash')
    msg = "\n".join(["{}={}".format(k, v) for k, v in sorted_params.items()])

    if param_hash == hmac.new(secret.digest(), msg.encode('utf-8'), digestmod=hashlib.sha256).hexdigest():
        return True
    return False


# работает
class StartSession(APIView):
    def post(self, request):
        print(request.data)
        if check_string(request.data):
            user_id = request.data['id']
            old_sessions = Session.objects.filter(user_id=user_id)
            old_sessions.delete()
            sess_hash = ''.join(random.choice(string.ascii_lowercase + string.ascii_uppercase + string.digits) for i in range(32))
            s = Session(user_id=user_id, sess_hash=sess_hash)
            s.save()
            return Response({'hash': sess_hash})
        else:
            return Response({'hash': ''})
            

class ManageQrs(APIView):
    # работает
    def get(self, request):
        print(request.query_params)
        try:
            sess_hash = request.query_params['hash']
            user_id = Session.objects.get(sess_hash=sess_hash).user_id
            qrs = QrCode.objects.filter(user_id=user_id)
            return Response({'qrs': QrSerializer(qrs, many=True).data})
        except:
            return Response({})

    # работает
    def post(self, request):
        print(request.data)
        try:
            sess_hash = request.data['hash']
            user_id = Session.objects.get(sess_hash=sess_hash).user_id
            url = request.data['url']
        except:
            return Response({'success': False})

        qr = QrCode(user_id=user_id, url=url, entries=0)

        try:
            name = request.data['name']
            qr.name = name
        except:
            pass

        qr.save()
        return Response({'success': True})


    def put(self, request):
        print(request.query_params)
        try:
            sess_hash = request.query_params['hash']
            id = request.query_params['id']
            qr = QrCode.objects.get(pk=id)
            session = Session.objects.get(sess_hash=sess_hash)
        except:
            return Response({'success': False})

        if (qr.user_id != session.user_id):
            return Response({'success': False})

        for field in request.query_params:
            if field != 'hash' and field != 'id':
                setattr(qr, field, request.query_params[field])
        qr.save()
        
        return Response({'success': True})


    def delete(self, request):
        print(request.query_params)
        try:
            sess_hash = request.query_params['hash']
            id = request.query_params['id']
            qr = QrCode.objects.get(pk=id)
            session = Session.objects.get(sess_hash=sess_hash)
        except:
            return Response({'success': False})

        if (qr.user_id != session.user_id):
            return Response({'success': False})

        try:
            qr.delete()
            return Response({'success': True})
        except:
            return Response({'success': False})


class TestApi(APIView):
    def get(self, request):
        # print(request.data)
        print(request.query_params)
        return Response({})

    def post(self, request):
        # print(request.data)
        print(request.query_params)
        return Response({})

    def put(self, request):
        # print(request.data)
        print(request.query_params)
        return Response({})

    def delete(self, request):
        #  print(request.data)
        print(request.query_params)
        return Response({})
    


def Redirect(request, id):
    try:
        qr = QrCode.objects.get(pk=id)
        qr.entries += 1
        qr.save()
        return HttpResponseRedirect('http://' + qr.url)
    except:
        return HttpResponse('Sorry, an error occuried')


def AppView(request, vue=None):
    return HttpResponse('aboba')