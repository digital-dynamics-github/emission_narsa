# -*- coding: utf-8 -*-


from django.contrib import admin
from contact.models import Contact, Person

# Register your models here.
class ContactAdmin(admin.ModelAdmin):
   list_display   = ('name', 'email', 'message')



admin.site.register(Contact, ContactAdmin)


class PersonAdmin(admin.ModelAdmin):
   list_display   = ('name', 'email', 'phone', "uid_ref", "uid")



admin.site.register(Person, PersonAdmin)
