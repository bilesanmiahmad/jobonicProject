from django.conf.urls import url
from django.conf.urls import include
from rest_framework.routers import DefaultRouter
from . import views


router = DefaultRouter()
# router.register('recruiter', views.JobonicUserViewSet)
# router.register('login', views.LoginViewSet, base_name='login')
router.register('profile', views.UserProfileViewSet)
router.register('seeker', views.JobonicJobberViewSet, base_name="seeker")
# router.register('activate', views.UserActivation, base_name="activate")

urlpatterns = [
    url(r'^activate/', views.UserActivation.as_view()),
    url(r'^login/$', views.LoginViewSet.as_view(), name=''),
    url(r'', include(router.urls)),
]
