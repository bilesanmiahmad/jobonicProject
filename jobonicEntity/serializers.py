from rest_framework import serializers
from .models import Entity, EntityProfile
from jobonicusers.models import JobonicUser
from jobonicusers.serializers import JobonicJobUserSerializer


class EntitySerializer(serializers.ModelSerializer):
    entity_admin = JobonicJobUserSerializer()

    class Meta:
        model = Entity
        fields = ('id', 'name', 'entity_admin', 'date_created', 'date_modified')
        extra_kwargs = {'date_created': {'read_only': True}, 'date_modified': {'read_only': True}}


class EntityProfileSerializer(serializers.ModelSerializer):
    entity = EntitySerializer

    class Meta:
        model = EntityProfile
        fields = ('id', 'entity', 'logo', 'primary_industry', 'about_company', 'phone', 'facebook', 'twitter', 'linkedIn', 'url', 'date_established', 'tags', 'location',
                  'company_size', 'country', 'date_created', 'date_modified')
        extra_kwargs = {'date_created': {'read_only': True}, 'date_modified': {'read_only': True}, }
