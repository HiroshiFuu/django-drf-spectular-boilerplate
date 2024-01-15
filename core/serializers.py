from django.contrib.auth import get_user_model

from rest_framework import serializers
from rest_framework.authtoken.serializers import AuthTokenSerializer


User = get_user_model()


class AuthTokenExampleSerializer(AuthTokenSerializer):

    class Meta:
        examples = {
            'username': 'user1',
            'password': '!234Rewq',
        }


class AuthUserSerializer(serializers.Serializer):
    username = serializers.CharField(label='Username')
    token = serializers.CharField(label='Token')

    class Meta:
        fields = ('username', 'token')
        examples = {
            'username': 'user1',
            'token': 'Bearer or Token',
        }


class UserSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()

    def get_full_name(self, obj):
        return '{} {}'.format(obj.first_name, obj.last_name)

    class Meta:
        model = User
        fields = ('id', 'full_name', 'email')
        examples = {
            'full_name': 'GivenName FamilyName',
            'email': 'E-mail',
        }


class AccountSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'username', 'password')
        extra_kwargs = {
            'username': {'required': True},
            'password': {'required': True},
        }
