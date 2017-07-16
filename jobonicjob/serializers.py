from rest_framework import serializers
from .models import Job


class JobSerializer(serializers.ModelSerializer):

    class Meta:
        model = Job
        fields = ('id', 'title', 'summary', 'description', 'entity', 'industry', 'creator', 'job_type', 'profession',
                  'min_qualification', 'min_experience', 'deadline_date', 'score', 'tags', 'job_status', 'date_created', 'is_created', 'is_published')
        extra_kwargs = {'date_created': {'read_only': True}, 'entity': {'read_only': True}, 'creator': {'read_only': True}, 'is_created': {'read_only': True}, 'is_published': {'read_only': True}}
