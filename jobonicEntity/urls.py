from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from . import views


router = DefaultRouter()
# View all companies. For admin purposes only
router.register('entity', views.EntityViewSet)
#
router.register('profile', views.EntityProfileViewSet)

# Contains endpoints to create a company
router.register('comp', views.CompanySignupViewSet, base_name='comp')
# router.register('test', views.TestCompanyViewSet, base_name='test')
urlpatterns = [
    url(r'', include(router.urls)),
    url(r'^signup/$', views.sign_up)

               ]
