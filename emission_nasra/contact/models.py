# -*- coding: utf-8 -*-

from django.db import models

# Create your models here.
TYPE = (
    ('pending', 'pending'),
    ('done', 'done'),
    ('error', 'error'),
)

class Contact(models.Model):

    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=254)
    message = models.TextField(blank=True)

    date = models.DateField(auto_now=True)
    date_created = models.DateField(auto_now_add=True)
    type = models.CharField(max_length=200, choices=TYPE, default="pending")

    def __id__(self):
        return self.id

    def __str__(self):
        return self.name




class Person(models.Model):

    name = models.CharField(max_length=200, blank=True, default="")
    email = models.EmailField(max_length=254, blank=True, default="")
    phone = models.CharField(max_length=25, blank=True, default="")
    uid = models.CharField(max_length=25, blank=True, default="")
    uid_ref = models.CharField(max_length=25, blank=True, default="")
    message = models.TextField(blank=True, default="")
    accept_reglement = models.BooleanField(blank=True, default=False)

    date = models.DateField(auto_now=True)
    date_created = models.DateField(auto_now_add=True)

    def __id__(self):
        return self.id

    def __str__(self):
        return self.name