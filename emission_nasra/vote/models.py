# -*- coding: utf-8 -*-

from django.db import models
from contact.models import Person
from candidat.models import Candidat, Project

# Create your models here.
class Vote(models.Model):
    person = models.ForeignKey(Person, blank=True, on_delete=models.CASCADE)
    candidat = models.ForeignKey(Candidat, blank=True, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, blank=True, on_delete=models.CASCADE)
    uid = models.CharField(max_length=200, default="", blank=True)


    date = models.DateField(auto_now=True)
    date_created = models.DateField(auto_now_add=True)

    def __id__(self):
        return self.id

    def __str__(self):
        return self.uid



class Reglement(models.Model):
    title = models.CharField(max_length=200, default="", blank=True)
    content = models.TextField( default="", blank=True)


    date = models.DateField(auto_now=True)
    date_created = models.DateField(auto_now_add=True)

    def __id__(self):
        return self.id

    def __str__(self):
        return self.title