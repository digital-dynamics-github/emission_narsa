# -*- coding: utf-8 -*-


from django.contrib import admin
from token_api.models import Token
# Register your models here.
class TokenAdmin(admin.ModelAdmin):
   list_display = ('id', "token", 'active', "day")


admin.site.register(Token, TokenAdmin)