import collections
import hmac
import hashlib
import string
import random

from django.conf import settings
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Session, QrCode
from .serializers import QrSerializer


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
    def get(self, request):
        sess_hash = request.query_params['hash']
        try:
            user_id = Session.objects.get(sess_hash=sess_hash).user_id
            qrs = QrCode.objects.filter(user_id=user_id)
            return Response({'qrs': QrSerializer(qrs, many=True).data})
        except:
            return Response({})
