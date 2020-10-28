# serializers.py

from rest_framework import serializers
from .models import Hero, Story

class HeroSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Hero
        fields = ('id', 'name', 'alias')

class StorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Story
        fields = ('id', 'headline', 'author', 'published_date', 'last_updated_date', 'text', 'slug')
