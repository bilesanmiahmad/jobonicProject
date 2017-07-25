from rest_framework import serializers
from .models import Industry, Profession, JobType, JobStatus, Country, EntitySize, ApplicationStage, CareerLevel, EducationLevel, Source
from jobonicusers.models import JobonicUser as User


class IndustrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Industry
        fields = ('id', 'name', 'date_created', 'created_by')
        created_by = serializers.ReadOnlyField(source='created_by.username')


class ProfessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profession
        fields = ('id', 'name', 'date_created', 'created_by')
        created_by = serializers.ReadOnlyField(source='created_by.username')


class JobTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobType
        fields = ('id', 'name', 'date_created', 'created_by')
        created_by = serializers.ReadOnlyField(source='created_by.username')


class JobStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobStatus
        fields = ('id', 'name', 'description', 'date_created', 'created_by')
        created_by = serializers.ReadOnlyField(source='created_by.username')


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ('id', 'name', 'date_created', 'created_by')
        created_by = serializers.ReadOnlyField(source='created_by.username')


class EntitySizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = EntitySize
        fields = ('id', 'size_info', 'date_created', 'created_by')
        created_by = serializers.ReadOnlyField(source='created_by.username')


class ApplicationStageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplicationStage
        fields = ('id', 'status', 'rank', 'date_created', 'created_by')
        created_by = serializers.ReadOnlyField(source='created_by.username')


class EducationLevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = EducationLevel
        fields = ('id', 'name', 'date_created', 'created_by')
        extra_kwargs = {'date_created': {'read_only': True}, 'created_by': {'read_only': True}}


class CareerLevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = CareerLevel
        fields = ('id', 'name', 'description', 'date_created', 'created_by')
        extra_kwargs = {'date_created': {'read_only': True}, 'created_by': {'read_only': True}}


class SourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Source
        fields = ('id', 'name', 'date_created', 'created_by')
        extra_kwargs = {'date_created': {'read_only': True}, 'created_by': {'read_only': True}}


class UserSerializer(serializers.ModelSerializer):
    industries = serializers.PrimaryKeyRelatedField(many=True, queryset=Industry.objects.all())
    professions = serializers.PrimaryKeyRelatedField(many=True, queryset=Profession.objects.all())
    job_types = serializers.PrimaryKeyRelatedField(many=True, queryset=JobType.objects.all())
    statuses = serializers.PrimaryKeyRelatedField(many=True, queryset=JobStatus.objects.all())
    countries = serializers.PrimaryKeyRelatedField(many=True, queryset=Country.objects.all())
    entity_sizes = serializers.PrimaryKeyRelatedField(many=True, queryset=EntitySize.objects.all())
    app_stages = serializers.PrimaryKeyRelatedField(many=True, queryset=ApplicationStage.objects.all())
    edu_levels = serializers.PrimaryKeyRelatedField(many=True, queryset=EducationLevel.objects.all())
    career_levels = serializers.PrimaryKeyRelatedField(many=True, queryset=CareerLevel.objects.all())

    class Meta:
        model = User
        fields = ('id', 'email', 'industries', 'professions', 'job_types', 'statuses', 'countries', 'entity_sizes', 'app_stages', 'edu_levels', 'career_levels')

