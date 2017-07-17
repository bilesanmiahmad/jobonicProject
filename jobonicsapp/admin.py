from django.contrib import admin
from .models import Industry, Country, EntitySize, ApplicationStage, CareerLevel, EducationLevel, Profession, JobStatus, JobType, Source
# Register your models here.

admin.site.register(Industry)
admin.site.register(Country)
admin.site.register(EntitySize)
admin.site.register(ApplicationStage)
admin.site.register(CareerLevel)
admin.site.register(EducationLevel)
admin.site.register(Profession)
admin.site.register(JobStatus)
admin.site.register(JobType)
admin.site.register(Source)

