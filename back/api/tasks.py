import time
from celery import shared_task
from .models import QrCode


@shared_task
def update_url(*args, **kwargs):
    qr_id = args[0]
    next_url_time = args[1]

    qr = QrCode.objects.get(id=qr_id)
    if qr.next_url_time != next_url_time:
        return False

    qr.url = qr.next_url
    qr.next_url = ""
    qr.next_url_time = ""
    qr.save()
    return True
