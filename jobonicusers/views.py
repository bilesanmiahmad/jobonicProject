from django.contrib.auth import authenticate
from rest_framework import viewsets
from rest_framework import views, response
from rest_framework import filters
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated, AllowAny
# Create your views here.

from jobonicusers import serializers, models, permissions


# class JobonicUserViewSet(viewsets.ModelViewSet):
#     """Handles creating, reading and updating users"""
#     serializer_class = serializers.JobonicUserSerializer
#     queryset = models.JobonicUser.objects.all()
#     authentication_classes = (TokenAuthentication,)
#     permission_classes = (permissions.UpdateBasicProfile,)
#     search_fields = ('first_name', 'last_name', 'email')
#     filter_backends = (filters.SearchFilter,)


class JobonicJobberViewSet(viewsets.ModelViewSet):
    """Handles creating, reading and updating users"""
    serializer_class = serializers.JobonicJobUserSerializer
    queryset = models.JobonicUser.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateBasicProfile,)
    search_fields = ('first_name', 'last_name', 'email')
    filter_backends = (filters.SearchFilter,)


class LoginViewSet(views.APIView):
    """Checks email and password and returns an auth token."""

    serializer_class = serializers.LoginSerializer
    permission_classes = (AllowAny,)

    def post(self, request):
        """Use the ObtainAuth Token APIView to validate and create a token"""
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token, created = Token.objects.get_or_create(user=user)
            user_serializer = serializers.JobonicJobUserSerializer(user)
            return response.Response(
                {'user': user_serializer.data, 'token': token.key}
            )

        return response.Response(
            {
                'error': 'Invalid email or password'
            }
        )


class UserProfileViewSet(viewsets.ModelViewSet):
    """Handles creating, reading and updating profile"""
    authentication_classes = (TokenAuthentication,)
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    permission_classes = (permissions.PostOwnProfile, IsAuthenticated,)

    def perform_create(self, serializer):
        """Sets the user profile to the logged in user."""
        serializer.save(user=self.request.user)
