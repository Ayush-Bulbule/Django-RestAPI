from email.errors import FirstHeaderLineIsContinuationDefect
from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken


class RegisterSerializer(serializers.Serializer):

    first_name = serializers.CharField()
    last_name = serializers.CharField()
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        if User.objects.filter(username=data['username']).exists():
            raise serializers.ValidationError('Username already exists')
        return data

    def create(self, validated_data):
        user = User.objects.create_user(
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            username=validated_data['username'].lower(),
        )
        user.set_password(validated_data['password'])
        return user


class LoginSerialzer(serializers.Serializer):

    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        if not User.objects.filter(username=data['username']).exists():
            raise serializers.ValidationError('Username does not exists')
        return data

    def get_jwt_token(self, data):
        user = authenticate(
            username=data['username'], password=data['password'])
        print(data['username'],data['password'])

        if not user:
            return {"message": "Invalid Credentials", "data": {}}

        refresh = RefreshToken.for_user(user)

        return{"message": "Login Successfull", "data": {"refresh": str(refresh), "access": str(refresh.access_token)}}
