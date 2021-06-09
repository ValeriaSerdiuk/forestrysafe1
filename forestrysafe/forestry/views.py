from django.shortcuts import render

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.generics import get_object_or_404, ListCreateAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.viewsets import ModelViewSet

from .models import Forestry, Animal, Feeder, Vaccination
from .serializers import ForestrySerializer, AnimalSerializer, FeederSerializer, VaccinationSerializer, \
    FeederCreateSerializer


class ForestryViewSet(generics.ListAPIView):
    serializer_class = ForestrySerializer

    def get_queryset(self):
        forestry = get_object_or_404(Forestry, pk=self.kwargs['pk'])
        return forestry.clients


class AnimalViewSet(generics.ListAPIView):
    serializer_class = AnimalSerializer

    def get_queryset(self):
        animal = get_object_or_404(Forestry, pk=self.kwargs['pk'])
        return animal.clients


class FeederViewSet(generics.ListAPIView):
    serializer_class = FeederSerializer

    def get_queryset(self):
        feeder = get_object_or_404(Feeder, pk=self.kwargs['pk'])
        return feeder.clients


class FeederCreateView(ListCreateAPIView):
    def get_permissions(self):
        if self.request.method == 'POST':
            self.permission_classes = [AllowAny]
        return super().get_permissions()

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return FeederCreateSerializer
        return FeederSerializer

    def get_queryset(self):
        feeder = get_object_or_404(Feeder, pk=self.kwargs['pk'])
        return Feeder.objects.filter(feeder_more__feeder=feeder)


class VaccinationViewSet(generics.ListAPIView):
    serializer_class = VaccinationSerializer

    def get_queryset(self):
        vaccination = get_object_or_404(Vaccination, pk=self.kwargs['pk'])
        return vaccination.clients


