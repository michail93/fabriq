from django.contrib.auth.models import User
from django.contrib.auth import authenticate

from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny

from .serializers import ApplicationSerializer, ApplicationInfoSerializer, GetUserTokenSerializer
from .models import Application


class AppListView(generics.ListCreateAPIView):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer


class AppView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer


class AppInfoView(generics.RetrieveAPIView):
    lookup_field = 'api_key'
    queryset = Application.objects.all()
    serializer_class = ApplicationInfoSerializer


class GetUserTokenView(generics.GenericAPIView):
    serializer_class = GetUserTokenSerializer
    permission_classes = (AllowAny, )

    def post(self, request, *args, **kwargs):
        serializer_class = self.get_serializer_class()
        serializer = serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = authenticate(username=serializer.data['username'], password=serializer.data['password'])

        if not user:
            user_data = User.objects.create_user(username=serializer.data['username'],
                                                 password=serializer.data['password'])
            Token.objects.create(user=user_data)

            return Response(data={'user_token': user_data.auth_token.key}, status=status.HTTP_201_CREATED)

        else:
            return Response(data={'user_token': user.auth_token.key}, status=status.HTTP_200_OK)
