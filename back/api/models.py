from django.db import models
from django.conf import settings
from django.core.files.base import ContentFile

from io import BytesIO
import qrcode
import qrcode.image.svg


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
    # отложенный урл
    next_url = models.TextField(max_length=8192, blank=True, default='')
    # время, на которое отложен урл
    next_url_time = models.CharField(max_length=20, blank=True, default='')
    # количество переходов по qr
    entries = models.IntegerField(default=0)
    # qrcode image
    image = models.ImageField(upload_to='qrs-images/', blank=True, null=True)

    def get_image(self):
        if self.image:
            return 'http://127.0.0.1:8000' + self.image.url

        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_H,
            box_size=10,
            border=4,
        )

        img = qrcode.make(settings.PROD_HOST + 'redirect/' + str(self.id) + '/',
                          image_factory=qrcode.image.svg.SvgPathImage)

        bytesIO = BytesIO(img.to_string())

        self.image.save(str(self.id) + '.svg',
                        ContentFile(bytesIO.getvalue()),
                        save=False)
        self.save()

        return 'http://127.0.0.1:8000' + self.image.url