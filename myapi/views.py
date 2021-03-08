from django.shortcuts import render
from rest_framework import viewsets
# Create your views here.
from .serializers import HeroSerializers, StudentSerializers
from .models import Hero, Student

class HeroViewSet(viewsets.ModelViewSet):
    queryset  = Hero.objects.all().order_by('name')
    serializer_class = HeroSerializers

class StudentViewSet(viewsets.ModelViewSet):
    queryset  = Student.objects.all().order_by('name')
    serializer_class = StudentSerializers
