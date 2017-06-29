from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from . import views


urlpatterns = [
    url(r'^industries/$', views.IndustryList.as_view()),
    url(r'^industries/(?P<pk>[0-9]+)/$', views.IndustryDetail.as_view()),
    url(r'^users/$', views.UserList.as_view()),
    url(r'users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view()),
    url(r'^professions/$', views.ProfessionList.as_view()),
    url(r'^jobtypes/$', views.JobTypeList.as_view()),
    url(r'^countries/$', views.CountryList.as_view()),
    url(r'^entity_sizes/$', views.EntitySizeList.as_view()),
    url(r'^app_stages/$', views.ApplicationStageList.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
