from rest_framework import generics

from .serializers import UserSerializer


class CreateUserView(generics.CreateAPIView):
    """create new user in system"""
    serializer_class = UserSerializer
