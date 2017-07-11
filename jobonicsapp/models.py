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
    name = models.CharField(max_length=20)
    created_by = models.ForeignKey(JobonicUser, related_name='countries', on_delete=models.CASCADE)
    date_created = models.DateField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Countries'

    def __str__(self):
        return self.name


class Industry(models.Model):
    name = models.CharField(max_length=20)
    date_created = models.DateField(auto_now=True)
    created_by = models.ForeignKey(JobonicUser, related_name='industries', on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Industries'

    def __str__(self):
        return self.name


class Profession(models.Model):
    name = models.CharField(max_length=20)
    date_created = models.DateField(auto_now=True)
    created_by = models.ForeignKey(JobonicUser, related_name='professions', on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Professions'

    def __str__(self):
        return self.name


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


class Job(models.Model):
    title = models.CharField(max_length=40)
    summary = models.TextField()
    description = models.TextField()
    entity = models.ForeignKey('jobonicEntity.Entity')
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

    class Meta:
        verbose_name_plural = 'Jobs'


class ApplicationStage(models.Model):
    status = models.CharField(max_length=20)
    rank = models.IntegerField()
    date_created = models.DateField(auto_now=True)
    created_by = models.ForeignKey(JobonicUser, related_name='app_stages', on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Application Stages'

    def __str__(self):
        return self.status


class Application(models.Model):
    applicant = models.ForeignKey(JobonicUser)
    job = models.ForeignKey(Job)
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


