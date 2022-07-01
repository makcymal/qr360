import hmac
import hashlib
import collections

from django.conf import settings

from rest_framework.response import Response
from rest_framework.views import APIView

from rest_registration.api.views.login import perform_login

from .models import QRUser


def check_string(data):
    secret = hashlib.sha256()
    secret.update(settings.TELEGRAM_BOT_TOKEN.encode('utf-8'))
    sorted_params = collections.OrderedDict(sorted(data.items()))
    param_hash = sorted_params.pop('hash')
    msg = "\n".join(["{}={}".format(k, v) for k, v in sorted_params.items()])

    if param_hash == hmac.new(secret.digest(), msg.encode('utf-8'), digestmod=hashlib.sha256).hexdigest():
        return True
    return False


class TelegramAuth(APIView):

    def post(self, request):
        try:
            if check_string(request.data):
                try:
                    user = QRUser.objects.get(username=request.data['id'])
                except QRUser.DoesNotExist:
                    user = QRUser.objects.create_user(username=request.data['id'])
                
                try:
                    extra_data = perform_login(request, user)
                    token = extra_data['token']

                    user.telegram_username = request.data['username']
                    user.photo_url = request.data['photo_url']
                    user.save()
                except:
                    return Response({'success': False, 'error': 'user create error'})

                return Response({
                    'success': True,
                    'token': token,
                    'username': user.telegram_username,
                    'photo_url': user.photo_url,
                })

            return Response({'success': False, 'error': 'invalid hash'})
        except:
            return Response({'success': False, 'error': 'incorrect request'})
