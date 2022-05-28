from rest_framework import fields, serializers
from .models import User, Session


class UserSerializer(serializers.ModelSerializer):
  class Meta:
		model = User
		fields = ("phone")


class SessionSerializer(serializers.ModelSerializer):
	class Meta:
		model = Session
		fields = ("session_hash")