from api.models import User, LogSolicitud
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class BitacoraSerializer(serializers.ModelSerializer):
    class Meta:
        model = LogSolicitud
        fields = "__all__"