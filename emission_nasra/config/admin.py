from django.contrib import admin
from config.models import *

# Register your models here.
class ConfigAdmin(admin.ModelAdmin):
   list_display   = ('name', 'type', 'key', 'value', "uid")



admin.site.register(Config, ConfigAdmin)