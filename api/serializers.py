from .models import Application
from rest_framework import serializers


class ApplicationSerializer(serializers.ModelSerializer):

    def validate_ID(self, value):
        if value <= 0:
            raise serializers.ValidationError("ID must be greater than 0")
        else:
            return value

    class Meta:
        model = Application
        exclude = ['api_key']


class ApplicationInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = '__all__'


class GetUserTokenSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=100)
    password = serializers.CharField(max_length=100)
