from django.contrib.auth import authenticate
from django.utils.translation import ugettext_lazy as _
from rest_framework import serializers

from .models import JobonicUser, JobonicUserManager, UserProfile


class LoginSerializer(serializers.Serializer):
    email = serializers.CharField(label=_("Email"))
    password = serializers.CharField(label=_("Password"), style={'input_type': 'password'})

    def create(self, validated_data):
        email = validated_data.get('email')
        password = validated_data.get('password')
        print(email, password)

        if email and password:
            user = authenticate(email=email, password=password)

            if user:
                if not user.is_active:
                    msg = _('User account is disabled.')
                    raise serializers.ValidationError(msg, code='authorization')
            else:
                msg = _('Unable to log in with providerdrr credentials.')
                raise serializers.ValidationError(msg, code='authorization')
        else:
            msg = _('Must include "username" and "password".')
            raise serializers.ValidationError(msg, code='authorization')

        return user


# class JobonicUserSerializer(serializers.ModelSerializer):
#     """To set up a user"""
#     class Meta:
#         model = JobonicUser
#         fields = ('id', 'first_name', 'middle_name', 'last_name', 'email', 'password',
#                   'date_created', 'date_joined', 'is_active', 'is_staff')
#         extra_kwargs = {'password': {'write_only': True}, 'is_active': {'read_only': True}, 'is_staff': {'read_only': True}, 'user_type': {'read_only': True}}
#
#     def create(self, validated_data):
#         """Create and return a user."""
#
#         user = JobonicUser(
#             first_name=validated_data['first_name'],
#             last_name=validated_data['last_name'],
#             email=validated_data['email'],
#         )
#
#         user.set_password(validated_data['password'])
#         user.save()
#
#         return user


class JobonicJobUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobonicUser
        fields = ('id', 'first_name', 'last_name', 'email', 'password',
                  'date_created', 'date_joined', 'is_active', 'is_staff')
        extra_kwargs = {'password': {'write_only': True}, 'is_active': {'read_only': True}, 'is_staff': {'read_only': True}}

    def create(self, validated_data):
        user = JobonicUser(
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            email=validated_data['email'],
        )

        user.set_password(validated_data['password'])
        user.save()

        return user


class UserProfileSerializer(serializers.ModelSerializer):
    """A serializer for user profile """

    class Meta:
        model = UserProfile
        fields = ('id', 'user', 'gender', 'birth_date',
                  'phone', 'facebook', 'twitter', 'linkedIn', 'created_on')
        extra_kwargs = {'user': {'read_only': True}, 'created_on': {'read_only': True}}
