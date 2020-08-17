from django.contrib.auth import get_user_model

from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    """serializer for users"""

    class Meta:
        model = get_user_model()
        fields = ('user', 'password', 'name')
        extra_kwargs = {'password': {'write_only': Tr}



