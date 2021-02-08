# -*- coding: utf-8 -*-


from django.contrib import admin
from jury.models import Jury

# Register your models here.
class JuryAdmin(admin.ModelAdmin):
   list_display   = ('first_name', 'last_name', 'uid')



admin.site.register(Jury, JuryAdmin)
