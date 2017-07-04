from django.shortcuts import render
from . import serializers
from . import models
from . import permissions

from rest_framework import viewsets
from rest_framework import filters
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.permissions import IsAuthenticated
# Create your views here.


class JobonicUserViewSet(viewsets.ModelViewSet):
    """Handles creating, reading and updating users"""
    serializer_class = serializers.JobonicUserSerializer
    queryset = models.JobonicUser.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateBasicProfile,)
    search_fields = ('first_name', 'last_name', 'email')
    filter_backends = (filters.SearchFilter, )


class LoginViewSet(viewsets.ViewSet):
    """Checks email and password and returns an auth token."""

    serializer_class = AuthTokenSerializer

    def create(self, request):
        """Use the ObtainAuth Token APIView to validate and create a token"""

        return ObtainAuthToken().post(request)


class UserProfileViewSet(viewsets.ModelViewSet):
    """Handles creating, reading and updating profile"""
    authentication_classes = (TokenAuthentication,)
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    permission_classes = (permissions.PostOwnProfile, IsAuthenticated,)

    def perform_create(self, serializer):
        """Sets the user profile to the logged in user."""
        serializer.save(user=self.request.user)
