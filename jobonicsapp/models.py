from django.db import models
from jobonicusers.models import JobonicUser
from django.contrib.auth.admin import UserAdmin

# Create your models here.


class Country(models.Model):
    name = models.CharField(max_length=20)
    created_by = models.ForeignKey(JobonicUser, related_name='countries', on_delete=models.CASCADE)
    date_created = models.DateField(auto_now=True)

    def __str__(self):
        return self.name


class EntitySize(models.Model):
    size_info = models.CharField(max_length=15)
    created_by = models.ForeignKey(JobonicUser, related_name='entity_sizes', on_delete=models.CASCADE)
    date_created = models.DateField(auto_now=True)

    def __str__(self):
        return self.size_info


class Entity(models.Model):
    name = models.CharField(max_length=50)
    logo = models.CharField(max_length=200)
    primary_industry = models.CharField(max_length=50)
    num_of_employees = models.IntegerField()
    about_company = models.TextField()
    facebook = models.CharField(max_length=50)
    linkedIn = models.CharField(max_length=50)
    twitter = models.CharField(max_length=50)
    url = models.CharField(max_length=50)
    date_established = models.DateField()
    organisation_type = models.CharField(max_length=20)
    tags = models.CharField(max_length=200)
    entity_admin = models.ForeignKey(JobonicUser)
    location = models.CharField(max_length=30)
    company_size = models.ForeignKey(EntitySize)
    country = models.ForeignKey(Country)
    company = models.ForeignKey('self', on_delete=models.CASCADE)
    date_created = models.DateField(auto_now_add=True)
    date_modified = models.DateField(auto_now=True)


class Industry(models.Model):
    name = models.CharField(max_length=20)
    date_created = models.DateField(auto_now=True)
    created_by = models.ForeignKey(JobonicUser, related_name='industries', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Profession(models.Model):
    name = models.CharField(max_length=20)
    date_created = models.DateField(auto_now=True)
    created_by = models.ForeignKey(JobonicUser, related_name='professions', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class JobType(models.Model):
    name = models.CharField(max_length=20)
    date_created = models.DateField(auto_now=True)
    created_by = models.ForeignKey(JobonicUser, related_name='job_types', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class JobStatus(models.Model):
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=100)
    date_created = models.DateField(auto_now=True)
    created_by = models.ForeignKey(JobonicUser, related_name='statuses', on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Job(models.Model):
    title = models.CharField(max_length=40)
    summary = models.TextField()
    description = models.TextField()
    entity = models.ForeignKey(Entity)
    industry = models.ForeignKey(Industry)
    creator = models.ForeignKey(JobonicUser)
    job_type = models.ForeignKey(JobType)
    profession = models.ForeignKey(Profession)
    min_qualification = models.CharField(max_length=100)
    min_experience = models.CharField(max_length=100)
    deadline_date = models.DateField()
    score = models.IntegerField()
    tags = models.CharField(max_length=100)
    date_created = models.DateField(auto_now=True)
    job_status = models.ForeignKey(JobStatus)


class ApplicationStage(models.Model):
    status = models.CharField(max_length=20)
    rank = models.IntegerField()
    date_created = models.DateField(auto_now=True)
    created_by = models.ForeignKey(JobonicUser, related_name='app_stages', on_delete=models.CASCADE)

    def __str__(self):
        return self.status


class Applications(models.Model):
    applicant = models.ForeignKey(JobonicUser)
    job = models.ForeignKey(Job)
    status = models.ForeignKey(ApplicationStage)
    match = models.IntegerField()
    date_created = models.DateField(auto_now=True)


class Schedule(models.Model):
    application = models.ForeignKey(Applications)
    schedule_date = models.DateField()
    schedule_time = models.TimeField()
    date_created = models.DateField(auto_now=True)
    created_by = models.ForeignKey(JobonicUser)
