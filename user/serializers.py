from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'user_id','password', 'email_id','age', 'phone', 'location','name']
        extra_kwargs = {'password': {'write_only': True}}   # this is only for hide pass

    def create(self, validated_data):
        return User.objects.create(**validated_data)
