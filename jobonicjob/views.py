from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import viewsets, status
from rest_framework.decorators import detail_route, list_route
from rest_framework.permissions import IsAuthenticated

from jobonicjob.models import Job
from jobonicjob.serializers import JobSerializer
from jobonicEntity.models import Entity


class JobViewSet(viewsets.ModelViewSet):
    queryset = Job.objects.all()
    serializer_class = JobSerializer

    @detail_route(methods=['put'])
    def publish(self, request, pk=None):
        queryset = Job.objects.all()
        job = get_object_or_404(queryset, pk=pk)
        serializer = JobSerializer(job)
        serializer.data['is_published'] = True
        return Response(serializer.data)

    def create_job(self, request):
        user = request.user.isAuthenticated
        site_user = request.user
        company = Entity.objects.get(entity_admin=site_user)
        if user:
            title = request.data['title']
            summary = request.data['summary']
            description = request.data['description']
            industry = request.data['industry']
            job_type = request.data['job_type']
            profession = request.data['profession']
            min_qualification = request.data['min_qualification']
            min_experience = request.data['min_experience']
            deadline_date = request.data['deadline_date']
            score = request.data['score']
            tags = request.data['tags']
            job_status = request.data['job_status']
            creator = site_user
            entity = company

            Job.objects.create(title=title, summary=summary, description=description, industry=industry, job_type=job_type,
                               profession=profession, min_qualification=min_qualification, min_experience=min_experience,
                               deadline_date=deadline_date, score=score, tags=tags, job_status=job_status, creator=creator,
                               entity=entity)
            return Response({
                "status_code": status.HTTP_201_CREATED,
                "message": "Job created"
            })
        else:
            return Response({
                "status_code": status.HTTP_401_UNAUTHORIZED,
                "message": "You do not have such permissions"
            })



