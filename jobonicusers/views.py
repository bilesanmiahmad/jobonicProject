from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
from django import core
from django.http import Http404
from rest_framework import status
from rest_framework import viewsets
from rest_framework import views, response
from rest_framework import filters
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import list_route, detail_route
# Create your views here.

from jobonicusers import serializers, models, permissions


# class JobonicUserViewSet(viewsets.ModelViewSet):
#     """Handles creating, reading and updating users"""
#     serializer_class = serializers.JobonicUserSerializer
#     queryset = models.JobonicUser.objects.all()
#     authentication_classes = (TokenAuthentication,)
#     permission_classes = (permissions.UpdateBasicProfile,)
#     search_fields = ('first_name', 'last_name', 'email')
#     filter_backends = (filters.SearchFilter,)


class JobonicJobberViewSet(viewsets.ViewSet):
    """Handles creating, reading and updating users"""
    serializer_class = serializers.JobonicJobUserSerializer
    queryset = models.JobonicUser.objects.all()
    # authentication_classes = (TokenAuthentication,)
    # permission_classes = (permissions.UpdateBasicProfile,)
    # search_fields = ('first_name', 'last_name', 'email')
    # filter_backends = (filters.SearchFilter,)

    @list_route(methods=('post',))
    def create_jobseeker(self, request):
        first_name = request.data['first_name']
        last_name = request.data['last_name']
        email = request.data['email']
        password = request.data['password']

        user = models.JobonicUser.objects.create_user(first_name=first_name, last_name=last_name, email=email, password=password)
        user = self.serializer_class(user)
        return response.Response({
            "message": "User created successfully",
            "status": status.HTTP_201_CREATED,
            "payload": user.data
        })


class LoginViewSet(views.APIView):
    """Checks email and password and returns an auth token."""

    serializer_class = serializers.LoginSerializer
    permission_classes = (AllowAny,)

    @list_route(methods=('post',))
    def post(self, request):
        """Use the ObtainAuth Token APIView to validate and create a token"""
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token, created = Token.objects.get_or_create(user=user)
            user_serializer = serializers.JobonicJobUserSerializer(user)
            return response.Response(
                {'user': user_serializer.data, 'token': token.key}
            )

        return response.Response(
            {
                'error': 'Invalid email or password'
            }
        )


class UserProfileViewSet(viewsets.ModelViewSet):
    """Handles creating, reading and updating profile"""
    authentication_classes = (TokenAuthentication,)
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    permission_classes = (permissions.PostOwnProfile, IsAuthenticated,)

    @list_route(methods=('POST',), url_path="user-profile")
    def create_profile(self, request):
        """Sets the user profile to the logged in user."""
        # serializer.save(user=self.request.user)
        user = request.user.is_authenticated()
        site_user = request.user
        if user:
            middle_name = request.data['middle_name']
            gender = request.data['gender']
            birth_date = request.data['birth_date']
            phone = request.data['phone']
            facebook = request.data['facebook']
            twitter = request.data['twitter']
            linkedIn = request.data['linkedIn']

            profile = models.UserProfile.objects.create(user=site_user, middle_name=middle_name, gender=gender,
                                                        birth_date=birth_date, phone=phone, facebook=facebook,
                                                        twitter=twitter, linkedIn=linkedIn)
            profile = self.serializer_class(profile)
            return response.Response({
                "status_code": status.HTTP_201_CREATED,
                "message": "Profile created",
                "payload": profile.data
            })
        else:
            return response.Response({
                "status_code": status.HTTP_401_UNAUTHORIZED,
                "message": "Profile created"
            })

    @list_route(methods=('GET',), permission_classes=(permissions.IsOwner,))
    def get_my_profile(self, request, *args, **kwargs):
        """
        Gets only your own profile
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        user = request.user.is_authenticated()
        site_user = request.user
        if user:
            my_profile = models.UserProfile.objects.filter(user=site_user)
            # my_profile_serialized = self.serializer_class(my_profile)
            my_profile_serialized = core.serializers.serialize('json', my_profile)

            return response.Response({
                "status_code": status.HTTP_200_OK,
                "message": "Profile returned",
                "result": my_profile_serialized
            })
        else:
            return response.Response({
                "status_code": status.HTTP_401_UNAUTHORIZED,
                "message": "You do not have permission to view this data."
            })


class UserActivation(views.APIView):
    permission_classes = (AllowAny,)
    def post(self, request):
        try:
            uuid_key = request.data.get("uuid_key")
            user = models.JobonicUser.objects.get(uuid_info=uuid_key)
        except models.JobonicUser.DoesNotExist:
            raise Http404("The requested object does not exist")
        user_serialized = serializers.JobonicJobUserSerializer(user)
        if user.is_activated:
            pass
        else:
            user.is_activated = True
        return response.Response({
            "status_code": status.HTTP_200_OK,
            "user": user_serialized.data
        })
