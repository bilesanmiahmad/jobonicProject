from django.contrib import admin
from .models import Industry, Country, EntitySize, ApplicationStage
# Register your models here.

admin.site.register(Industry)
admin.site.register(Country)
admin.site.register(EntitySize)
admin.site.register(ApplicationStage)
