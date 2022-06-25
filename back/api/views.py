import json
import sys

from urllib.parse import urlencode
from urllib.request import Request, build_opener

from django.conf import settings

from rest_framework.response import Response
from rest_framework.views import APIView


def get_remote_ip():
    f = sys._getframe()
    while f:
        request = f.f_locals.get("request")
        if request:
            remote_ip = request.META.get("REMOTE_ADDR", "")
            forwarded_ip = request.META.get("HTTP_X_FORWARDED_FOR", "")
            ip = remote_ip if not forwarded_ip else forwarded_ip
            return ip
        f = f.f_back


def recaptcha_request(params):
    request_object = Request(
        url="https://www.google.com/recaptcha/api/siteverify",
        data=params,
    )

    opener = build_opener()

    return opener.open(request_object)


class Recaptcha(APIView):

    def post(self, request):
        try:
            secret_key = settings.RECAPTCHA_SECRET_KEY
            recaptcha_response = request.data['recaptchaToken']
            remote_ip = get_remote_ip()
        except:
            pass
            return Response({'success': False})

        params = urlencode({
            "secret": secret_key,
            "response": recaptcha_response,
            "remoteip": remote_ip,
        })
        
        params = params.encode("utf-8")

        response = recaptcha_request(params)
        data = json.loads(response.read().decode("utf-8"))
        response.close()

        return Response({
            'success': data.pop('success'),
            'error-codes': data.pop("error-codes", None),
            'extra_data': data,
        })
