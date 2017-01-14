from __future__ import unicode_literals

from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)


class Project(models.Model):
    title = models.CharField(max_length=200)
    client = models.CharField(max_length=200)
    description = models.TextField()
    service = models.ForeignKey('Service')
    finished_date = models.DateTimeField(blank=True, null=True)


class Service(models.Model):
    name = models.CharField(max_length=200)

    def __unicode__(self):
        return self.name
