from django.contrib.auth.hashers import make_password
from rest_framework import generics
from users.models import User
from users.serializers import UserSerializer


class UserCreationApiView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def perform_create(self, serializer):
        password = serializer.validated_data['password']
        hashed_password = make_password(password)
        serializer.save(password=hashed_password)
