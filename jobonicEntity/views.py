from rest_framework import generics, permissions, filters, viewsets, status, response
from rest_framework.response import Response
from rest_framework.decorators import list_route
from rest_framework.permissions import AllowAny

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


class CompanyProfileViewSet(viewsets.ViewSet):
    serializer_class = EntityProfileSerializer

    @list_route(methods=('post',), url_path="create-profile")
    def create_profile(self, request):
        user = request.user.is_authenticated()
        site_user = request.user
        if user:
            company = Entity.objects.filter(entity_admin=site_user)
            if company is not None:
                entity = company
                logo = request.data['logo']
                primary_industry = request.data['primary_industry']
                about_company = request.data['about_company']
                phone = request.data['phone']
                facebook = request.data['facebook']
                twitter = request.data['twitter']
                linkedIn = request.data['linkedIn']
                url = request.data['url']
                date_established = request.data['date_established']
                tags = request.data['tags']
                location = request.data['location']
                company_size = request.data['company_size']
                country = request.data['country']
                company_profile = EntityProfile.objects.create(entity=entity, logo=logo,
                                                               primary_industry=primary_industry,
                                                               about_company=about_company,
                                                               phone=phone, facebook=facebook, twitter=twitter,
                                                               linkedIn=linkedIn,
                                                               url=url, date_established=date_established,
                                                               tags=tags, location=location, company_size=company_size,
                                                               country=country)
                return response.Response({
                    "message": "Profile created successfully",
                    "status": status.HTTP_201_CREATED,
                    "payload": company_profile.data
                })


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
