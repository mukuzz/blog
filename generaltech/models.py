from operator import mod
from django.db import models
from django.utils import timezone


class Author(models.Model):
    username = models.CharField(blank=True, max_length=256)
    twitter = models.CharField(blank=True, max_length=256)
    name = models.CharField(blank=True, max_length=256)
    about = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(blank=True, max_length=64)
    slug = models.CharField(blank=True, max_length=64)

    def __str__(self):
        return self.name


class Article(models.Model):
    uri = models.CharField(blank=False, max_length=256)
    title = models.TextField(blank=True)
    description = models.TextField(blank=True)
    titleImage = models.ImageField(upload_to="image/")
    content = models.TextField(blank=True)
    published = models.BooleanField(default=False)
    tags = models.ManyToManyField(Tag)
    authors = models.ManyToManyField(Author)
    publish_time = models.DateTimeField(default=timezone.now)
    update_time = models.DateTimeField(default=timezone.now)
    related_articles = models.ManyToManyField("self", blank=True)

    def __str__(self):
        return self.uri