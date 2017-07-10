from django.shortcuts import render
from .models import Entity, EntityProfile
from .serializers import EntityProfileSerializer, EntitySerializer
from rest_framework import generics, permissions, filters, viewsets

# Create your views here.


class EntityViewSet(viewsets.ModelViewSet):
    """Create, Read, Update and Delete entities"""
    queryset = Entity.objects.all()
    serializer_class = EntitySerializer
    permission_classes = permissions.IsAuthenticated


class EntityProfileViewSet(viewsets.ModelViewSet):
    """Create, Read, Update and Delete entity profiles"""
    queryset = EntityProfile.objects.all()
    serializer_class = EntityProfileSerializer
    permission_classes = permissions.IsAuthenticatedOrReadOnly
