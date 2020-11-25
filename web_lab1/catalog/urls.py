from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('company', views.CompanyAPIView)
router.register('industry', views.IndustryAPIView)
router.register('vacancy', views.VacancyAPIView)
router.register('city', views.CityAPIView)
router.register('application', views.ApplicationAPIView)

urlpatterns = [
    path('', include(router.urls)),
]
