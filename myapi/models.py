from django.db import models
from django.utils import timezone

class Hero(models.Model):
    name = models.CharField(max_length=60)
    alias = models.CharField(max_length=60)

    def __str__(self):
        return self.name

class Story(models.Model):
    headline = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    published_date = models.DateTimeField(auto_now=False, auto_now_add=True)
    last_updated_date = models.DateTimeField(auto_now=True, auto_now_add=False)
    text = models.TextField()
    slug = models.SlugField()

    def __str__(self):
        return self.slug
