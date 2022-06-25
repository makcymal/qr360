from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils import timezone

from .managers import QRUserManager


def qruser_directory_path(instance, filename):
    return f'qrusers/{instance.id}/{filename}'


class QRUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=32, unique=True)
    telegram_id = models.PositiveBigIntegerField(blank=True, null=True)
    photo_url = models.TextField(max_length=8192, blank=True, null=True)

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    objects = QRUserManager()

    class Meta:
        ordering = ('username', )

    def __str__(self):
        return self.username
