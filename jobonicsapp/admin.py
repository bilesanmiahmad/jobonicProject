from django.contrib import admin
from .models import Industry, Profession, Country, EntitySize, JobStatus, JobType, ApplicationStage
# Register your models here.

admin.site.register(Industry)
admin.site.register(Profession)
admin.site.register(Country)
admin.site.register(EntitySize)
admin.site.register(JobType)
admin.site.register(JobStatus)
admin.site.register(ApplicationStage)
