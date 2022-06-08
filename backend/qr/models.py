from django.db import models
import qrcode
import qrcode.image.svg
from io import BytesIO
from PIL import Image
from django.core.files import File
from django.core.files.base import ContentFile


class Session(models.Model):
    user_id = models.IntegerField(default=0)
    sess_hash = models.CharField(max_length=128)


class QrCode(models.Model):
    # telegram id
    user_id = models.IntegerField(default=0)
    # куда надо редиректить, при сканировании qr
    redirect_url = models.TextField(max_length=8192)
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

        img = qrcode.make('qr360.tk/' + str(self.id) + '/',
                          image_factory=qrcode.image.svg.SvgPathImage)

        bytesIO = BytesIO(img.to_string())

        self.image.save(str(self.id) + '.svg',
                        ContentFile(bytesIO.getvalue()),
                        save=False)
        self.save()

        return 'http://127.0.0.1:8000' + self.image.url
