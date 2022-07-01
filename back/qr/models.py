from io import BytesIO
import qrcode
import qrcode.image.svg

from django.db import models
from django.conf import settings
from django.core.files.base import ContentFile

from users.models import QRUser


def get_byte_qrimage(content):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )

    img = qrcode.make(content, image_factory=qrcode.image.svg.SvgPathImage)

    bytesIO = BytesIO(img.to_string())

    return bytesIO.getvalue()


def qr_directory_path(instance, filename):
    return f'qrs/{instance.qruser.id}/{filename}'


def qrdemo_directory_path(instance, filename):
    return f'qrs/demo/{filename}'


class QRModel(models.Model):
    qruser = models.ForeignKey(QRUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, blank=True, default='')
    url = models.TextField(max_length=8192)
    entries = models.IntegerField(default=0)
    next_url = models.TextField(max_length=8192, blank=True, default='')
    next_url_time = models.CharField(max_length=20, blank=True, default='')
    image = models.ImageField(upload_to=qr_directory_path,
                              blank=True,
                              null=True)

    class Meta:
        ordering = ('name', )

    def __str__(self):
        return self.qruser.username + ' ' + str(self.id)

    def get_image(self):
        if self.image:
            return str(settings.CURRENT_HOST) + self.image.url

        self.image.save(str(self.id) + '.svg',
                        ContentFile(
                            get_byte_qrimage(
                                str(settings.CURRENT_HOST) + '/redirect/' +
                                str(self.id) + '/')),
                        save=False)
        self.save()

        return str(settings.CURRENT_HOST) + self.image.url


class DemoQR(models.Model):
    url = models.TextField(max_length=8192)
    image = models.ImageField(upload_to=qrdemo_directory_path,
                              blank=True,
                              null=True)

    def get_image(self):
        if self.image:
            return str(settings.CURRENT_HOST) + self.image.url

        self.image.save(str(self.id) + '.svg',
                        ContentFile(
                            get_byte_qrimage(
                                str(settings.CURRENT_HOST) +
                                '/demo-redirect/' + str(self.id) + '/')),
                        save=False)
        self.save()

        return str(settings.CURRENT_HOST) + self.image.url

    def __str__(self):
        return str(self.id)
