# -*- coding: utf-8 -*-

from django.db import models

# Create your models here.

TYPE_CONFIG = (
    ('stream', 'stream'),
    ('vote', 'vote'),
    ('tombola', 'tombola'),
    ('jauge_candidat', 'jauge_candidat'),
)
# Create your models here.
class Config(models.Model):
    name = models.CharField(max_length=200, blank=True)
    uid = models.CharField(max_length=200, blank=True)
    type = models.CharField(max_length=200, choices=TYPE_CONFIG, blank=True, default="")
    key = models.CharField(max_length=200, blank=True)
    value = models.CharField(max_length=200, blank=True)
    active = models.BooleanField(blank=False, default=True)


    def __id__(self):
        return self.id

    def __str__(self):
        return self.name