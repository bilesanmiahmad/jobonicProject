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

    # def create(self, validated_data):
    #     admin_user = validated_data.pop('user')
    #     company = Entity.objects.create(**validated_data)
    #     JobonicUser.objects.create(company=company, **admin_user)
    #     return company


class EntityProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = EntityProfile
        fields = ('id', 'entity', 'logo', 'primary_industry', 'about_company', 'facebook', 'twitter', 'linkedIn', 'url', 'date_established', 'tags', 'location',
                  'company_size', 'country', 'date_created', 'date_modified')
        extra_kwargs = {'date_created': {'read_only': True}, 'date_modified': {'read_only': True}}


class EntityUserSerializer(serializers.Serializer):
    first_name = serializers.CharField(max_length=50)
    last_name = serializers.CharField(max_length=50)
    email = serializers.EmailField()
    company = serializers.CharField(max_length=70)
    phone = serializers.CharField(max_length=15)
    company_email = serializers.EmailField()

    # def create(self, validated_data):
    #     fname = validated_data.get('first_name')
    #     lname = validated_data.get('last_name')
    #     email = validated_data.get('email')
    #     user = JobonicUser(fname, lname, email)
    #     user.set_password(validated_data['password'])
    #     user.save()
    #
    #     company = validated_data.get('company')
    #     phone = validated_data.get('phone')
    #     c_email = validated_data.get('company_email')
    #     entity = Entity(company, phone, c_email)
    #     entity.save()
    #     return [user, entity]
    # def update(self, instance, validated_data):
    #     pass


