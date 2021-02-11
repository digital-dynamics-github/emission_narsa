# -*- coding: utf-8 -*-

from django.db import models

# Create your models here.


class Project(models.Model):
    uid = models.CharField(max_length=200, blank=True, default="")
    title = models.CharField(max_length=200, blank=True, default="")
    title_ar = models.CharField(max_length=200, blank=True, default="")
    second_title = models.CharField(max_length=200, blank=True, default="")
    second_title_ar = models.CharField(max_length=200, blank=True, default="")
    content = models.TextField(blank=True, default="")
    content_ar = models.TextField(blank=True, default="")
    cover = models.ImageField(upload_to="uploads/project/cover", null=True, blank=True)
    video = models.TextField(blank=True, default="")
    category = models.CharField(max_length=200, blank=True, default="")
    category_ar = models.CharField(max_length=200, blank=True, default="")

    date = models.DateField(auto_now=True)
    date_created = models.DateField(auto_now_add=True)

    def __id__(self):
        return self.id

    def __str__(self):
        return self.title

class Candidat(models.Model):
    project = models.ForeignKey(Project, blank=True, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=200, blank=True, default="")
    first_name_ar = models.CharField(max_length=200, blank=True, default="")
    last_name = models.CharField(max_length=200, blank=True, default="")
    last_name_ar = models.CharField(max_length=200, blank=True, default="")
    email = models.CharField(max_length=254, blank=True, default="")
    site_web = models.CharField(max_length=254, blank=True, default="")
    facebook = models.CharField(max_length=254, blank=True, default="")
    twitter = models.CharField(max_length=254, blank=True, default="")
    about = models.TextField(blank=True,default="")
    about_ar = models.TextField(blank=True,default="")
    position = models.CharField(max_length=254, blank=True,default="")
    position_ar = models.CharField(max_length=254, blank=True,default="")
    company = models.CharField(max_length=254, blank=True,default="")
    company_ar = models.CharField(max_length=254, blank=True,default="")
    photo = models.ImageField(upload_to="uploads/candidat/candidat", null=True, blank=True)
    total_votes = models.IntegerField(blank=True, default="0")
    pourcent_votes = models.FloatField(blank=True, default="0")
    uid = models.CharField(max_length=200, blank=True, default="")

    date = models.DateField(auto_now=True)
    date_created = models.DateField(auto_now_add=True)

    def __id__(self):
        return self.id

    def __str__(self):
        return self.first_name


