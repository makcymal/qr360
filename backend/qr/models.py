from django.db import models


class Session(models.Model):
    user_id = models.IntegerField(default=0)
    sess_hash = models.CharField(max_length=32)


class QrCode(models.Model):
    # telegram id
    user_id = models.IntegerField(default=0)
    # название, опционально
    name = models.CharField(max_length=50, blank=True, default='')
    # куда надо редиректить, при сканировании qr
    url = models.TextField(max_length=8192)
    # количество переходов по qr
    entries = models.IntegerField(default=0)
