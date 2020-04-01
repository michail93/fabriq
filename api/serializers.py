from .models import Application
from rest_framework import serializers


class ApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        exclude = ['api_key']


class ApplicationInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = '__all__'


class CreateUserSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=100)
    password = serializers.CharField(max_length=100)


class GetUserTokenSerializer(CreateUserSerializer):
    pass
