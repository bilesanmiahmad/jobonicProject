from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.decorators import detail_route

from .models import Job
from .serializers import JobSerializer


class JobViewSet(viewsets.ModelViewSet):
    queryset = Job.objects.all()
    serializer_class = JobSerializer


class PublishViewSet(viewsets.ViewSet):
    @detail_route(methods=['put'])
    def publish(self, request, pk=None):
        queryset = Job.objects.all()
        job = get_object_or_404(queryset, pk=pk)
        serializer = JobSerializer(job)
        serializer.data['is_published'] = True
        return Response(serializer.data)
