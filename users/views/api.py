from rest_framework import generics, permissions, status, views
from rest_framework.response import Response
from django.contrib.auth import authenticate, login

from ..models import User
from ..serializers import CustomUserSerializer, LoginSerializer


class CustomUserCreate(generics.CreateAPIView):
    serializer_class = CustomUserSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        return User.objects.all()


class LoginView(views.APIView):
    serializer_class = LoginSerializer
    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = authenticate(**serializer.validated_data)

        if user:
            login(request, user)
            return Response(self.serializer_class(user).data)
        else:
            return Response(
                {"error": "Wrong Credentials"},
                status=status.HTTP_400_BAD_REQUEST,
            )
