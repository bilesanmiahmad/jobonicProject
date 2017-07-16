from django.db import models

# Create your models here.


class Job(models.Model):
    title = models.CharField(max_length=40)
    summary = models.TextField()
    description = models.TextField()
    entity = models.ForeignKey('jobonicEntity.Entity')
    industry = models.ForeignKey('jobonicsapp.Industry')
    creator = models.ForeignKey('jobonicusers.JobonicUser')
    job_type = models.ForeignKey('jobonicsapp.JobType')
    profession = models.ForeignKey('jobonicsapp.Profession')
    min_qualification = models.CharField(max_length=100)
    min_experience = models.CharField(max_length=100)
    deadline_date = models.DateField()
    score = models.IntegerField()
    tags = models.CharField(max_length=100)
    date_created = models.DateField(auto_now=True)
    job_status = models.ForeignKey('jobonicsapp.JobStatus')
    is_created = models.BooleanField(default=True)
    is_published = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = 'Jobs'
