# -*- coding: utf-8 -*-

from django.db import models

# Create your models here.
class Jury(models.Model):
    uid = models.CharField(max_length=200, blank=True, default="")
    first_name = models.CharField(max_length=200, blank=True, default="")
    first_name_ar = models.CharField(max_length=200, blank=True, default="")
    last_name = models.CharField(max_length=200, blank=True, default="")
    last_name_ar = models.CharField(max_length=200, blank=True, default="")
    email = models.EmailField(max_length=254, blank=True, default="")
    site_web = models.CharField(max_length=254, blank=True, default="")
    facebook = models.CharField(max_length=254, blank=True, default="")
    twitter = models.CharField(max_length=254, blank=True, default="")
    about = models.TextField(blank=True,default="")
    about_ar = models.TextField(blank=True,default="")
    position = models.TextField(blank=True,default="")
    position_ar = models.TextField(blank=True,default="")
    company = models.TextField(blank=True,default="")
    company_ar = models.TextField(blank=True,default="")
    photo = models.ImageField(upload_to="uploads/jury/jury", null=True, blank=True)

    date = models.DateField(auto_now=True)
    date_created = models.DateField(auto_now_add=True)

    def __id__(self):
        return self.id

    def __str__(self):
        return self.first_name