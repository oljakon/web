from .models import Industry, Company, JobVacancy, Application, City
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics, permissions, viewsets, mixins

from .serializers import CitySerializer, CompanySerializer, IndustrySerializer, VacancySerializer, ApplicationSerializer

class CityAPIView(viewsets.ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class CompanyAPIView(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class IndustryAPIView(viewsets.ModelViewSet):
    queryset = Industry.objects.all()
    serializer_class = IndustrySerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class VacancyAPIView(viewsets.ModelViewSet):
    queryset = JobVacancy.objects.all()
    serializer_class = VacancySerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class ApplicationAPIView(viewsets.ModelViewSet):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
