from rest_framework import generics, permissions, filters, viewsets

from django.shortcuts import render
from django.http.response import HttpResponse

from jobonicEntity.models import Entity, EntityProfile
from jobonicusers.models import JobonicUser as JobUser, JobonicUser
from jobonicEntity.serializers import EntityProfileSerializer, EntitySerializer, EntityUserSerializer
from jobonicEntity.forms import LoginForm

# Create your views here.


class EntityViewSet(viewsets.ModelViewSet):
    """Create, Read, Update and Delete entities"""
    queryset = Entity.objects.all()
    serializer_class = EntitySerializer
    # permission_classes = permissions.IsAuthenticated

    # def list(self, request, *args, **kwargs):
    #     queryset = self.Entity.objects.all()
    #     serializer = EntitySerializer(self.get_queryset())
    #     return HttpResponse(serializer.data)


class EntityProfileViewSet(viewsets.ModelViewSet):
    """Create, Read, Update and Delete entity profiles"""
    queryset = EntityProfile.objects.all()
    serializer_class = EntityProfileSerializer
    # permission_classes = permissions.IsAuthenticatedOrReadOnly


class CompanySignupViewSet(viewsets.ViewSet):

    def create(self, request):
        first_name = request.data['first_name']
        last_name = request.data['last_name']
        email = request.data['email']
        phone = request.data['phone']
        company = request.data['comp_name']
        website = request.data['website']
        password = request.data['password']

        user = JobUser.objects.create_user(email=email, password=password, first_name=first_name, last_name=last_name, phone=phone)
        entity = Entity.objects.create(name=company, url=website, entity_admin=user)
        user.company = entity
        user.save()

        return HttpResponse("Thanks")


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

            user = JobUser.objects.create_user(email=email, password=password, first_name=first_name, last_name=last_name, phone=phone)
            Entity.objects.create(name=company, url=website, entity_admin=user)

            return HttpResponse("Thanks")
    else:
        form = LoginForm()
    return render(request, 'signup.html', {'form': form})

