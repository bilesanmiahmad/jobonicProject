from .models import Industry, Country, ApplicationStage, EntitySize, EducationLevel, CareerLevel, Profession, JobType, JobStatus
from .serializers import IndustrySerializer, ProfessionSerializer, JobStatusSerializer, JobTypeSerializer, UserSerializer, CountrySerializer, ApplicationStageSerializer, EntitySizeSerializer, EducationLevelSerializer, CareerLevelSerializer
from rest_framework import generics, permissions, viewsets, filters
from jobonicusers.models import JobonicUser as User

# Create your views here.


class IndustryViewSet(viewsets.ModelViewSet):
    """Create, read, update, and delete industries"""
    queryset = Industry.objects.all()
    serializer_class = IndustrySerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)


class ProfessionViewSet(viewsets.ModelViewSet):
    """Create, read, update, delete professions"""
    queryset = Profession.objects.all()
    serializer_class = ProfessionSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)


class JobTypeViewSet(viewsets.ModelViewSet):
    """Create, read, update, delete Job types"""
    queryset = JobType.objects.all()
    serializer_class = JobTypeSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)


class JobStatusViewSet(viewsets.ModelViewSet):
    """Create, read, update, delete Job Status"""
    queryset = JobStatus.objects.all()
    serializer_class = JobStatusSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)


class CountryViewSet(viewsets.ModelViewSet):
    """Create, read, update, delete Job Status"""
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)


class EntitySizeViewSet(viewsets.ModelViewSet):
    """Create, read, update, delete Entity size"""
    queryset = EntitySize.objects.all()
    serializer_class = EntitySizeSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)


class ApplicationStageViewSet(viewsets.ModelViewSet):
    """Create, read, update, delete Application stages"""
    queryset = ApplicationStage.objects.all()
    serializer_class = ApplicationStageSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)


class EducationLevelViewSet(viewsets.ModelViewSet):
    """Create, read, update, delete Education Levels"""
    queryset = EducationLevel.objects.all()
    serializer_class = EducationLevelSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)


class CareerLevelViewSet(viewsets.ModelViewSet):
    """Create, read, update, delete Career Levels"""
    queryset = CareerLevel.objects.all()
    serializer_class = CareerLevelSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
