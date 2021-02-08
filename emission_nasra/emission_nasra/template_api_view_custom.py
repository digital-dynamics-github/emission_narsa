# -*- coding: utf-8 -*-


import time
from django.utils.translation import gettext as _
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.http import JsonResponse
from rest_framework import status
import uuid

from emission_nasra.middleware import TokenCheck



class TemplateAPIViewCustom(APIView):
    accepted_renderer = True
    renderer_classes = (JSONRenderer,)
    permission_classes = (AllowAny,)
    security = True

    def checkToken(self, token):
        token_check = TokenCheck()
        return token_check.check(token)

    def generateUID(self):
        return str(uuid.uuid4())[:8]



    def dispatch(self, request, *args, **kwargs):

        if 'token_api' in request.GET :
            token_api = request.GET["token_api"]
            check_security_token = self.checkToken(token_api)

            if self.security == True and check_security_token == False:

                response = Response(
                    {"status": "error", "data": [], "count": 0, "message": _("Token of API is not Valid or Expired")},
                    content_type="application/json", status=200)

                response.accepted_renderer = JSONRenderer()
                response.accepted_media_type = "application/json"
                response.renderer_context = {}

                return response
            else:
                return super(TemplateAPIViewCustom, self).dispatch(request, *args, **kwargs)
        else:

            response = Response(
                {"status": "error", "data": [], "count": 0, "message": _("Token is Required to make this Request")},
                content_type="application/json", status=status.HTTP_401_UNAUTHORIZED)

            response.accepted_renderer = JSONRenderer()
            response.accepted_media_type = "application/json"
            response.renderer_context = {}

            return response








