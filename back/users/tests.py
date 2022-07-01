from django.contrib.auth import get_user_model
from django.test import TestCase


class QRUserManagerTests(TestCase):

    def test_create_user(self):
        UserModel = get_user_model()
        qruser = UserModel.objects.create_user(username='test',
                                               password='test')
        
        self.assertEqual(qruser.username, 'test')
        self.assertTrue(qruser.is_active)
        self.assertFalse(qruser.is_staff)
        self.assertFalse(qruser.is_superuser)
        
        with self.assertRaises(TypeError):
            UserModel.objects.create_user()
        with self.assertRaises(ValueError):
            UserModel.objects.create_user(username='')
        with self.assertRaises(ValueError):
            UserModel.objects.create_user(username='', password='test')

    def test_create_superuser(self):
        UserModel = get_user_model()
        qruser_admin = UserModel.objects.create_superuser(username='test',
                                                          password='test')
        
        self.assertEqual(qruser_admin.username, 'test')
        self.assertTrue(qruser_admin.is_active)
        self.assertTrue(qruser_admin.is_staff)
        self.assertTrue(qruser_admin.is_superuser)
        
        with self.assertRaises(ValueError):
            UserModel.objects.create_superuser(username='test',
                                               password='test',
                                               is_superuser=False)
