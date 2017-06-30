from django.contrib.auth.models import User
from uploads.models import Upload
from rest_framework import serializers


class AuthUploadsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Upload
        fields = ('uploaded', 'description','file', 'key')
        read_only_fields = ('key',)


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username', 'uploads')
