from django.db import models
from jobonicusers.models import JobonicUser
from django.contrib.auth.admin import UserAdmin

# Create your models here.


class EntitySize(models.Model):
    size_info = models.CharField(max_length=15)
    created_by = models.ForeignKey(JobonicUser, related_name='entity_sizes', on_delete=models.CASCADE)
    date_created = models.DateField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Entity Sizes'

    def __str__(self):
        return self.size_info


class Country(models.Model):
    name = models.CharField(max_length=30)
    created_by = models.ForeignKey(JobonicUser, related_name='countries', on_delete=models.CASCADE)
    date_created = models.DateField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Countries'

    def __str__(self):
        return self.name


class Industry(models.Model):
    name = models.CharField(max_length=50)
    date_created = models.DateField(auto_now=True)
    created_by = models.ForeignKey(JobonicUser, related_name='industries', on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Industries'

    def __str__(self):
        return self.name


class ApplicationStage(models.Model):
    status = models.CharField(max_length=20)
    rank = models.IntegerField()
    date_created = models.DateField(auto_now=True)
    created_by = models.ForeignKey(JobonicUser, related_name='app_stages', on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Application Stages'

    def __str__(self):
        return self.status


class JobType(models.Model):
    name = models.CharField(max_length=20)
    date_created = models.DateField(auto_now=True)
    created_by = models.ForeignKey(JobonicUser, related_name='job_types', on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Job Types'

    def __str__(self):
        return self.name


class JobStatus(models.Model):
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=100)
    date_created = models.DateField(auto_now=True)
    created_by = models.ForeignKey(JobonicUser, related_name='statuses', on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Job Statuses'

    def __str__(self):
        return self.title


class Profession(models.Model):
    name = models.CharField(max_length=50)
    date_created = models.DateField(auto_now=True)
    created_by = models.ForeignKey(JobonicUser, related_name='professions', on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Professions'

    def __str__(self):
        return self.name


class Application(models.Model):
    applicant = models.ForeignKey(JobonicUser)
    job = models.ForeignKey('jobonicjob.Job')
    status = models.ForeignKey(ApplicationStage)
    match = models.IntegerField()
    date_created = models.DateField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Applications'


class Schedule(models.Model):
    application = models.ForeignKey(Application)
    schedule_date = models.DateField()
    schedule_time = models.TimeField()
    date_created = models.DateField(auto_now=True)
    created_by = models.ForeignKey(JobonicUser)

    class Meta:
        verbose_name_plural = 'Schedules'


class EducationLevel(models.Model):
    name = models.CharField(max_length=20)
    date_created = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(JobonicUser)

    class Meta:
        verbose_name_plural = 'Educational Levels'

    def __str__(self):
        return self.name


class CareerLevel(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=50)
    date_created = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(JobonicUser)

    class Meta:
        verbose_name_plural = 'Career Levels'

    def __str__(self):
        return self.name
