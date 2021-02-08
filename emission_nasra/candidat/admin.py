# -*- coding: utf-8 -*-


from django.contrib import admin
from candidat.models import *

# Register your models here.
class CandidatAdmin(admin.ModelAdmin):
   list_display   = ('first_name', 'last_name', 'email', 'about', "uid", "total_votes")



admin.site.register(Candidat, CandidatAdmin)


class ProjectAdmin(admin.ModelAdmin):
   list_display   = ('title', 'content', 'uid')



admin.site.register(Project, ProjectAdmin)
