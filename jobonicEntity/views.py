from rest_framework import generics, permissions, filters, viewsets, status, response
from rest_framework.response import Response
from rest_framework.decorators import list_route
import sendgrid
from rest_framework.permissions import AllowAny
import requests

from django.shortcuts import render
from django.http.response import HttpResponse

from jobonicEntity.models import Entity, EntityProfile
from jobonicusers.models import JobonicUser as JobUser, JobonicUser
from jobonicEntity.serializers import EntityProfileSerializer, EntitySerializer
from jobonicEntity.forms import LoginForm
from keys import *


# Create your views here.


class EntityViewSet(viewsets.ModelViewSet):
    """Create, Read, Update and Delete entities"""
    queryset = Entity.objects.all()
    serializer_class = EntitySerializer
    # permission_classes = permissions.AllowAny

    # def list(self, request, *args, **kwargs):
    #     queryset = self.Entity.objects.all()
    #     serializer = EntitySerializer(self.get_queryset())
    #     return HttpResponse(serializer.data)


class EntityProfileViewSet(viewsets.ModelViewSet):
    """Create, Read, Update and Delete entity profiles"""
    queryset = EntityProfile.objects.all()
    serializer_class = EntityProfileSerializer
    permission_classes = permissions.AllowAny


# class CompanyProfileViewSet(viewsets.ViewSet):
#     serializer_class = EntityProfileSerializer
#
#     @list_route(methods=('post',), url_path="create-profile")
#     def create_profile(self, request):


class CompanySignupViewSet(viewsets.ViewSet):
    serializer_class = EntitySerializer
    # Create a new company profile -- https://jobonicplatform.com/api/company/comp/create

    @list_route(methods=('post',), url_path="create-account", permission_classes=[AllowAny])
    def create_account(self, request):
        print("Create")
        first_name = request.data['first_name']
        last_name = request.data['last_name']
        email = request.data['email']
        company = request.data['comp_name']
        password = request.data['password']

        user = JobUser.objects.create_user(email=email, password=password, first_name=first_name, last_name=last_name)
        entity = Entity.objects.create(name=company, entity_admin=user)
        user.company = entity
        user.save()
        user = self.serializer_class(entity)
        return response.Response({
            "message": "Company created successfully",
            "status": status.HTTP_201_CREATED,
            "payload": user.data
        })


def sign_up(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['pc_email']
            phone = form.cleaned_data['pc_phone']
            company = form.cleaned_data['comp_name']
            website = form.cleaned_data['website']
            password = form.cleaned_data['password']

            user = JobUser.objects.create_user(email=email, password=password, first_name=first_name,
                                               last_name=last_name, phone=phone)
            Entity.objects.create(name=company, url=website, entity_admin=user)

            return HttpResponse("Thanks")
    else:
        form = LoginForm()
    return render(request, 'signup.html', {'form': form})
