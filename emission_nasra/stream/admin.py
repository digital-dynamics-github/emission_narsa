# -*- coding: utf-8 -*-


from django.contrib import admin
from stream.models import Stream

# Register your models here.
class StreamAdmin(admin.ModelAdmin):
   list_display   = ('title', 'description', 'code', 'active', 'uid')



admin.site.register(Stream, StreamAdmin)
