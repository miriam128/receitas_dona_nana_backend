from rest_framework import serializers
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def validate_email(self, value):
      if User.objects.filter(email=value).exists():
          raise serializers.ValidationError("Este e-mail já está em uso.")
      return value
    
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user