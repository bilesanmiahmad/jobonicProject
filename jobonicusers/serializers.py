from rest_framework import serializers
from .models import JobonicUser, JobonicUserManager, UserProfile


class JobonicUserSerializer(serializers.ModelSerializer):
    """To set up a user"""
    class Meta:
        model = JobonicUser
        fields = ('id', 'first_name', 'middle_name', 'last_name', 'email', 'password',
                  'date_created', 'date_joined', 'is_active', 'is_staff')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        """Create and return a user."""

        user = JobonicUser(
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            email=validated_data['email']
        )

        user.set_password(validated_data['password'])
        user.save()

        return user


class UserProfileSerializer(serializers.ModelSerializer):
    """A serializer for user profile """

    class Meta:
        model = UserProfile
        fields = ('id', 'user', 'gender', 'birth_date', 'user_type',
                  'phone', 'facebook', 'twitter', 'linkedIn', 'created_on')
        extra_kwargs = {'user': {'read_only': True}}
