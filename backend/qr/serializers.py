from rest_framework import serializers

from .models import QrCode


class QrSerializer(serializers.ModelSerializer):
    class Meta:
        model = QrCode
        fields = ('id', 'name', 'url', 'entries')

    