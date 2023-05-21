from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model


class UserRegister(serializers.ModelSerializer):

    password2=serializers.CharField(style={'input_type':'password'},write_only=True)

    class Meta:
        model = User
        