from .models import Industry, Company, JobVacancy, Application, City
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics, permissions, viewsets, mixins

from .serializers import CitySerializer, CompanySerializer, IndustrySerializer, VacancySerializer, ApplicationSerializer


class CityAPIView(mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.DestroyModelMixin,
                      mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer

    def get_permissions(self):
        if self.request.method == 'DELETE' or self.request.method == 'POST':
            return [permissions.IsAdminUser()]
        elif self.request.method == 'GET':
            return [permissions.AllowAny()]


class CompanyAPIView(mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.DestroyModelMixin, \
                     mixins.ListModelMixin, mixins.UpdateModelMixin, viewsets.GenericViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

    def get_permissions(self):
        if self.request.method == 'DELETE' or self.request.method == 'POST' or self.request.method == 'PATCH' \
                or self.request.method == 'PUT':
            return [permissions.IsAdminUser()]
        elif self.request.method == 'GET':
            return [permissions.AllowAny()]


class IndustryAPIView(mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.DestroyModelMixin,
                      mixins.ListModelMixin, mixins.UpdateModelMixin, viewsets.GenericViewSet):
    queryset = Industry.objects.all()
    serializer_class = IndustrySerializer

    def get_permissions(self):
        if self.request.method == 'DELETE' or self.request.method == 'POST' or self.request.method == 'PATCH' \
                or self.request.method == 'PUT':
            return [permissions.IsAdminUser()]
        elif self.request.method == 'GET':
            return [permissions.AllowAny()]


class VacancyAPIView(mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.DestroyModelMixin,
                      mixins.ListModelMixin, mixins.UpdateModelMixin, viewsets.GenericViewSet, ):
    queryset = JobVacancy.objects.all()
    serializer_class = VacancySerializer
    filterset_fields = '__all__'
    search_fields = ('title', 'body')

    def get_permissions(self):
        if self.request.method == 'DELETE' or self.request.method == 'POST' or self.request.method == 'PATCH' \
                or self.request.method == 'PUT':
            return [permissions.IsAdminUser()]
        elif self.request.method == 'GET':
            return [permissions.AllowAny()]


class ApplicationAPIView(mixins.CreateModelMixin, mixins.DestroyModelMixin,
                      mixins.ListModelMixin, mixins.UpdateModelMixin, viewsets.GenericViewSet):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer

    def get_permissions(self):
        if self.request.method == 'DELETE':
            return [permissions.IsAdminUser()]
        elif self.request.method == 'GET':
            return [permissions.AllowAny()]
        elif self.request.method == 'POST' or self.request.method == 'PATCH' or self.request.method == 'PUT':
            return [permissions.IsAuthenticated()]