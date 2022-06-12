from rest_framework import serializers

from .models import QrCode


class QrSerializer(serializers.ModelSerializer):
    class Meta:
        model = QrCode
        fields = ('id', 'name', 'url', 'next_url', 'next_url_time', 'entries', 'get_image')
