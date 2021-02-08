# -*- coding: utf-8 -*-


from django.shortcuts import render, redirect
from django.views.generic import TemplateView

import time




from django.db.models import Q


from emission_nasra.middleware import MobileDetection

import uuid
from config.models import Config


class TemplateViewSite(TemplateView):

    menus = {}
    widgets = {}
    blocks = {}
    language = "ar"
    apply_view = False
    custom_view = None
    name = "home"
    path_theme = None
    messages = []
    login = False
    redirection_author = False
    redirection_user = False

    def generateUID(self):
        return str(uuid.uuid4())[:8]


    def mergQuery(self, q1, q2):
        return self.mergeQuery(q1, q2)

    def mergeQuery(self, q1, q2):
        q3 = q1.union(q2)
        q3 = q3.distinct()
        return q3




    def dispatch(self, request, *args, **kwargs):

        domain = request.META["HTTP_HOST"]


        return super(TemplateViewSite, self).dispatch(request, *args, **kwargs)




