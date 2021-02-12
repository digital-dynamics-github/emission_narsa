# -*- coding: utf-8 -*-

from django.db import models

# Create your models here.
class Stream(models.Model):
    uid = models.CharField(max_length=200, blank=True, default="")
    title = models.CharField(max_length=200, blank=True, default="")
    title_ar = models.CharField(max_length=200, blank=True, default="")
    description = models.TextField(blank=True,default="")
    description_ar = models.TextField(blank=True,default="")
    code = models.TextField(blank=True,default="")
    code_ar = models.TextField(blank=True,default="")
    photo = models.ImageField(upload_to="uploads/stream/stream", null=True, blank=True)
    active = models.BooleanField(blank=True, default=False)

    date = models.DateField(auto_now=True)
    date_created = models.DateField(auto_now_add=True)

    def __id__(self):
        return self.id

    def __str__(self):
        return self.title




class BlockText(models.Model):
    uid = models.CharField(max_length=200, blank=True, default="")
    title = models.CharField(max_length=200, blank=True, default="")
    title_ar = models.CharField(max_length=200, blank=True, default="")
    description = models.TextField(blank=True,default="")
    description_ar = models.TextField(blank=True,default="")
    location = models.CharField(max_length=250, blank=True,default="")

    date = models.DateField(auto_now=True)
    date_created = models.DateField(auto_now_add=True)

    def __id__(self):
        return self.id

    def __str__(self):
        return self.title
