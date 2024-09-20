from django.contrib.auth import authenticate, get_user_model
from django.http import JsonResponse
from django.shortcuts import render
from django_tenants.utils import schema_context
from rest_framework import generics, renderers, permissions, status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, mixins, status
from dreametrix.models import User

from api.serializers import UserSerializer
from rest_framework.authtoken.models import Token
from dreametrix.models import School





def index(request):
    return JsonResponse({"nothing": "nothing"})

class UserCreate(mixins.CreateModelMixin, mixins.ListModelMixin, generics.GenericAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    renderer_classes = (renderers.JSONRenderer,)

    def post(self, request, *args, **kwargs):
        print("entering")
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.save()
            return Response({"email": user.email}, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

register_view = UserCreate.as_view()



class UserLogin(APIView):
    def post(self, request, *arg,  **kwargs):
        data = request.data
        email = data.get("email")
        password = data.get("password")
        user = authenticate(request, email=email, password=password)
        if user:
            token, _ = Token.objects.get_or_create(user=user)
            return Response({'email': user.email, 'token': token.key}, status=status.HTTP_200_OK)
        return Response({"message": "wrong credentials"}, status=status.HTTP_400_BAD_REQUEST)

login_view = UserLogin.as_view()



