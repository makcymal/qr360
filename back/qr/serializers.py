from rest_framework import serializers

from .models import DemoQR, QRModel


class QRModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = QRModel
        fields = (
            'id',
            'name',
            'url',
            'entries',
            'next_url',
            'next_url_time',
            'get_image',
        )


class DemoQRSerializer(serializers.ModelSerializer):

    class Meta:
        model = DemoQR
        fields = (
            'id',
            'url',
            'get_image',
        )
