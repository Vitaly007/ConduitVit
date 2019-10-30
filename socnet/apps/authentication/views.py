from rest_framework import status
from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from datetime import datetime,timedelta
from rest_framework.renderers import TemplateHTMLRenderer

from .models import User

from .serializers import (
    RegistrationSerializer, LoginSerializer, UserSerializer)
from .renderers import UserJSONRenderer


class RegistrationAPIView(APIView):
    # Allow any user (authenticated or not) to hit this endpoint.
    permission_classes = (AllowAny,)
    #renderer_classes = (UserJSONRenderer,)  
    serializer_class = RegistrationSerializer
	

		
    def post(self, request):
        user = request.data.get('user', {})
        if not user:
            user = {
                "email": request.data.get('email'),
                "username": request.data.get('username'),
                "password": request.data.get('password')
            }
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)
	
	

class LoginAPIView(APIView):
    permission_classes = (AllowAny, )
    serializer_class = LoginSerializer

    def post(self, request):
        user = request.data.get('user', {})
        if not user:
            user = {
                "email": request.data.get('email'),				
                "password": request.data.get('password')
            }
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)

        email = serializer['email'].value
        token = serializer['token'].value   #serializer.data['token']
        response_data = {
            'access_token': token,
            'email': email
        }
        expiration = (datetime.utcnow() + timedelta(days=10))
        response = Response(serializer.data, status=status.HTTP_200_OK)
        response.set_cookie('token', response_data['access_token'])
        response.set_cookie('email', response_data['email'])
        return response

class UserRetrieveUpdateAPIView(RetrieveUpdateAPIView):
    permission_classes = (IsAuthenticated,)
    renderer_classes = (UserJSONRenderer,)
    serializer_class = UserSerializer

    def retrieve(self, request, *args, **kwargs):
        # There is nothing to validate or save here. Instead, we just want the
        # serializer to handle turning our `User` object into something that
        # can be JSONified and sent to the client.
        serializer = self.serializer_class(request.user)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def update(self, request, *args, **kwargs):
        user_data = request.data.get('user', {})

        serializer_data = {
            'username': user_data.get('username', request.user.username),
            'email': user_data.get('email', request.user.email),

            'profile': {
                'bio': user_data.get('bio', request.user.profile.bio),
                'image': user_data.get('image', request.user.profile.image)
            }
        }

        # Here is that serialize, validate, save pattern we talked about
        # before.
        serializer = self.serializer_class(
            request.user, data=serializer_data, partial=True
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_200_OK)
		
