from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from rest_api.models import Training, Person
from rest_api.serializer import PersonSerializer, TrainingSerializer

# Create your views here.


def index(request):
    return HttpResponse('NOT AVAILABLE')


class PeopleViewSet(viewsets.ModelViewSet):
    """Show all People"""
    queryset = Person.objects.all()
    serializer_class = PersonSerializer


class TraininsViewSet(viewsets.ModelViewSet):
    """Show All Trainings"""
    queryset = Training.objects.all()
    serializer_class = TrainingSerializer

