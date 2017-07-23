import uuid

from django.db import models

from jobonicusers.models import JobonicUser

# Create your models here.


class Entity(models.Model):
    name = models.CharField(max_length=50)
    entity_admin = models.ForeignKey(JobonicUser)
    date_created = models.DateField(auto_now_add=True)
    date_modified = models.DateField(auto_now=True)

    def __str__(self):
        return self.name


class EntityProfile(models.Model):
    entity = models.OneToOneField(Entity)
    logo = models.URLField(max_length=200)
    primary_industry = models.ForeignKey('jobonicsapp.Industry')
    about_company = models.TextField()
    facebook = models.CharField(max_length=70)
    linkedIn = models.CharField(max_length=70)
    twitter = models.CharField(max_length=70)
    url = models.CharField(max_length=70)
    date_established = models.DateField()
    tags = models.CharField(max_length=200)
    location = models.CharField(max_length=30)
    company_size = models.ForeignKey('jobonicsapp.EntitySize')
    country = models.ForeignKey('jobonicsapp.Country')
    uuid_data = models.UUIDField(unique=True, default=uuid.uuid4, editable=False)
    is_activated = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{0}--Profile'.format(self.entity.name)
