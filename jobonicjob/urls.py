from django.conf.urls import include, url
from rest_framework.routers import DefaultRouter
from .views import JobViewSet


router = DefaultRouter()
router.register('job', JobViewSet)
urlpatterns = [url(r'', include(router.urls)), ]
