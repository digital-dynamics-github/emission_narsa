# -*- coding: utf-8 -*-


from django.contrib import admin
from stream.models import Stream, BlockText

# Register your models here.
class StreamAdmin(admin.ModelAdmin):
   list_display   = ('title', 'description', 'code', 'active', 'uid')



admin.site.register(Stream, StreamAdmin)


class BlockTextAdmin(admin.ModelAdmin):
   list_display   = ('title', 'description', 'location',  'uid')



admin.site.register(BlockText, BlockTextAdmin)
