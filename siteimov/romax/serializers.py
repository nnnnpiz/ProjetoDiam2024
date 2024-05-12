from dataclasses import fields

from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Cliente
class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields =['username', 'password']