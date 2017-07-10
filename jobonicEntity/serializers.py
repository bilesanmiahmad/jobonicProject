from rest_framework import serializers
from .models import Entity, EntityProfile


class EntitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Entity
        fields = ('id', 'name', 'entity_admin', 'telephone', 'email', 'date_created', 'date_modified')
        extra_kwargs = {'entity_admin': {'read_only': True}, 'date_created': {'read_only': True}, 'date_modified': {'read_only': True}}


class EntityProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = EntityProfile
        fields = ('id', 'entity', 'logo', 'primary_industry', 'about_company', 'facebook', 'twitter', 'linkedIn', 'url', 'date_established', 'tags', 'location',
                  'company_size', 'country', 'date_created', 'date_modified')
        extra_kwargs = {'date_created': {'read_only': True}, 'date_modified': {'read_only': True}}
