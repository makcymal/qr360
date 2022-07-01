from django.test import TestCase

from qr.models import QRModel
from users.models import QRUser


def QRModelTest(TestCase):

    def setUp(self):
        qruser = QRUser.objects.create(username='test')
        QRModel.objects.create(qruser=qruser, url='test.me')

    def test_image_path(self):
        qruser = QRUser.objects.get(username='test')
        qr = QRModel.objects.get(qruser=qruser)
        qr.get_image()
        self.assertEqual(qr.image.url, f'{qruser.id}/{qr.image.name}')
