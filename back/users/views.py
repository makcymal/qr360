import hmac
import hashlib
import time

from django.conf import settings

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import authentication

from rest_registration.api.views.login import perform_login

from .models import QRUser


class TelegramAuth(APIView):

    def post(self, request):
        if not request.session.exists(request.session.session_key):
            request.session.create()

        bot_token = settings.TELEGRAM_BOT_TOKEN
        if bot_token is None:
            return Response({'success': False})

        received_hash_string = request.data['hash']
        auth_date = request.data['auth_date']

        if received_hash_string is None or auth_date is None:
            return Response({'success': False})

        data_check_string = [
            f'{k}={v}' for k, v in request.data.items() if k != 'hash'
        ]
        data_check_string = '\n'.join(sorted(data_check_string))
        secret_key = hashlib.sha256(bot_token.encode()).digest()
        built_hash = hmac.new(secret_key,
                              msg=data_check_string.encode(),
                              digestmod=hashlib.sha256).hexdigest()

        current_timestamp = int(time.time())
        auth_timestamp = int(auth_date)

        if current_timestamp - auth_timestamp > 86400:
            return Response({'success': False})
        if built_hash != received_hash_string:
            return Response({'success': False})

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
            return Response({'success': False})

        return Response({
            'success': True,
            'token': token,
            'username': user.telegram_username,
            'photo_url': user.photo_url,
        })
