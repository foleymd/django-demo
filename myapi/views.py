from django.shortcuts import render

from rest_framework import viewsets

from .serializers import HeroSerializer, StorySerializer
from .models import Hero, Story


class HeroViewSet(viewsets.ModelViewSet):
    queryset = Hero.objects.all().order_by('name')
    serializer_class = HeroSerializer

class StoryViewSet(viewsets.ModelViewSet):
    queryset = Story.objects.all().order_by('last_updated_date')
    serializer_class = StorySerializer
