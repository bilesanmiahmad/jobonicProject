from django.contrib import admin
from .models import EntityProfile, Entity

# Register your models here.
admin.site.register(Entity)
admin.site.register(EntityProfile)
