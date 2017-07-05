from django.conf.urls import url
from django.conf.urls import include
from rest_framework.routers import DefaultRouter
from . import views


router = DefaultRouter()
router.register('recruiter', views.JobonicUserViewSet)
router.register('login', views.LoginViewSet, base_name='login')
router.register('profile', views.UserProfileViewSet)
router.register('seeker', views.JobonicJobberViewSet)

urlpatterns = [url(r'', include(router.urls)), ]
