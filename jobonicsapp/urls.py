from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.routers import DefaultRouter
from . import views


router = DefaultRouter()
router.register('industries', views.IndustryViewSet)
router.register('professions', views.ProfessionViewSet)
router.register('jobtypes', views.JobTypeViewSet)
router.register('jobstatus', views.JobStatusViewSet)
router.register('countries', views.CountryViewSet)
router.register('entitysize', views.EntitySizeViewSet)
router.register('appstages', views.ApplicationStageViewSet)
router.register('careers-levels', views.CareerLevelViewSet)
router.register('edu-levels', views.EducationLevelViewSet)
urlpatterns = [
    # url(r'^industries/$', views.IndustryList.as_view()),
    # url(r'^industries/(?P<pk>[0-9]+)/$', views.IndustryDetail.as_view()),
    # url(r'^users/$', views.UserList.as_view()),
    # url(r'users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view()),
    # url(r'^professions/$', views.ProfessionList.as_view()),
    # url(r'^jobtypes/$', views.JobTypeList.as_view()),
    # url(r'^countries/$', views.CountryList.as_view()),
    # url(r'^entity_sizes/$', views.EntitySizeList.as_view()),
    # url(r'^app_stages/$', views.ApplicationStageList.as_view()),
    url(r'', include(router.urls))
]
