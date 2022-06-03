from django.db import models


class Session(models.Model):
    user_id = models.IntegerField(default=0)
    sess_hash = models.CharField(max_length=32)


class QrCode(models.Model):
    # telegram id
    user_id = models.IntegerField(default=0)
    # куда надо редиректить, при сканировании qr
    redirect_url = models.TextField(max_length=8192)
    # ссылка, которая шифруется в qr
    const_url = models.CharField(max_length=255)
    # количество переходов по qr
    entries = models.IntegerField(default=0)
