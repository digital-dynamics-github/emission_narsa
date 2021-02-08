# -*- coding: utf-8 -*-


from django.contrib import admin
from vote.models import Vote, Reglement
# Register your models here.
class VoteAdmin(admin.ModelAdmin):
   list_display = ('id', "person", 'candidat', "project", "uid")


admin.site.register(Vote, VoteAdmin)

class ReglementAdmin(admin.ModelAdmin):
   list_display = ('id', "title", 'content')


admin.site.register(Reglement, ReglementAdmin)