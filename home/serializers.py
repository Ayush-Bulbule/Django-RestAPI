from email.errors import FirstHeaderLineIsContinuationDefect
from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken

from .models import Blog
 


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        exclude = ["created_at", "updated_at"]

