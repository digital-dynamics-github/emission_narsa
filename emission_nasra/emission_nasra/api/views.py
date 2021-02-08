# -*- coding: utf-8 -*-

from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework.permissions import AllowAny, IsAuthenticated

from emission_nasra.template_api_view_custom import TemplateAPIViewCustom
from stream.models import Stream
from config.models import Config
from candidat.models import Candidat, Project
from contact.models import Person
from vote.models import Vote, Reglement
from jury.models import Jury
import os


from django.core.files.base import ContentFile
import base64

class ActiveWidget(TemplateAPIViewCustom):
    permission_classes = (AllowAny,)
    renderer_classes = (JSONRenderer,)
    limit_per_page = 10

    def get(self, request, type, uid):
        message = "تمت العملية بنجاح"
        status = "success"
        widget = None
        active = False
        if type == "active_stream":
            widget = Stream.objects.all().filter(uid=uid)


        if type == "active_vote":
            widget = Config.objects.all().filter(type="vote")


        if not widget == None:
            if widget.count() == 1:
                widget = widget[0]
                print(widget.active)
                if widget.active == True:
                    widget.active = False
                else:
                    if type == "active_stream":
                        streams_active = Stream.objects.all().filter(active=True)
                        if streams_active.count() > 0:
                            for str_act in streams_active:
                                str_act.active = False
                                str_act.save()
                    widget.active= True

                widget.save()
                active = widget.active



        return Response({ "status" : status, "message" : message, "active" : active }, content_type="application/json", status=200)

class SaveStream(TemplateAPIViewCustom):
    permission_classes = (AllowAny,)
    renderer_classes = (JSONRenderer,)
    limit_per_page = 10

    def post(self, request):
        message = "تمت العملية بنجاح"
        status = "success"

        data = request.data

        stream = Stream()
        stream.title = data["title"]
        stream.description = data["description"]
        stream.code = data["code"]
        stream.uid = self.generateUID()

        streams_active = Stream.objects.all().filter(active=True)
        if streams_active.count() > 0:
            for str_act in streams_active:
                str_act.active = False
                str_act.save()

        stream.active = True
        stream.save()


        return Response({ "status" : status, "message" : message, }, content_type="application/json", status=200)

class SaveReglement(TemplateAPIViewCustom):
    permission_classes = (AllowAny,)
    renderer_classes = (JSONRenderer,)
    limit_per_page = 10

    def post(self, request):
        message = "تمت العملية بنجاح"
        status = "success"

        data = request.data

        reglement = Reglement()
        reglement.title = data["title"]
        reglement.content = data["content"]
        reglement.save()


        return Response({ "status" : status, "message" : message, }, content_type="application/json", status=200)

class UpdateReglement(TemplateAPIViewCustom):
    permission_classes = (AllowAny,)
    renderer_classes = (JSONRenderer,)
    limit_per_page = 10

    def post(self, request, uid):
        message = "تمت العملية بنجاح"
        status = "success"

        data = request.data

        reglement = Reglement.objects.all().filter(id=int(uid))
        if reglement.count() == 1:
            reglement = reglement[0]
            reglement.title = data["title"]
            reglement.content = data["content"]
            reglement.save()


        return Response({ "status" : status, "message" : message, }, content_type="application/json", status=200)



class GetReglement(TemplateAPIViewCustom):
    permission_classes = (AllowAny,)
    renderer_classes = (JSONRenderer,)
    limit_per_page = 10

    def get(self, request, uid):
        message = "تمت العملية بنجاح"
        status = "success"

        data = None

        reglement = Reglement.objects.all().filter(id=int(uid))
        if reglement.count() == 1:
            reglement = reglement[0]
            data = { "title" : reglement.title, "content" : reglement.content }



        return Response({ "status" : status, "message" : message, "data" : data }, content_type="application/json", status=200)


class SaveCandidat(TemplateAPIViewCustom):
    permission_classes = (AllowAny,)
    renderer_classes = (JSONRenderer,)
    limit_per_page = 10

    def post(self, request):
        message = "تمت العملية بنجاح"
        status = "success"

        data = request.data

        project = Project()
        project.title = data["title_project"]
        project.second_title = data["second_title_project"]
        project.content = data["content_project"]
        project.video = data["video_project"]

        project.uid = self.generateUID()

        project.save()


        candidat = Candidat()
        candidat.project = project
        candidat.first_name = data["first_name"]
        candidat.last_name = data["last_name"]
        candidat.email = data["email"]
        candidat.site_web = data["site_web"]
        candidat.facebook = data["facebook"]
        candidat.twitter = data["twitter"]
        candidat.position = data["position"]
        candidat.company = data["company"]
        candidat.uid = self.generateUID()

        photo_base_64 = data["photo_base64"]

        if not photo_base_64 == "" and not photo_base_64 == "photo":
            format, imgstr = photo_base_64.split(';base64,')
            ext = format.split('/')[-1]
            file_name = str(candidat.uid) + "." + ext
            try:
                os.remove(candidat.photo.path)
            except:
                a = ""

        if not photo_base_64 == "" and not photo_base_64 == "photo":
            format, imgstr = photo_base_64.split(';base64,')
            ext = format.split('/')[-1]
            data_file = ContentFile(base64.b64decode(imgstr))
            file_name = str(candidat.uid) + "." + ext
            candidat.photo.save(file_name, data_file, save=True)

        candidat.save()


        return Response({ "status" : status, "message" : message, }, content_type="application/json", status=200)


class SavePerson(TemplateAPIViewCustom):
    permission_classes = (AllowAny,)
    renderer_classes = (JSONRenderer,)
    limit_per_page = 10

    def post(self, request):
        message = "merci pour votre vote"
        status = "success"

        data = request.data

        uid_ref = None
        candidat = Candidat.objects.all().filter(uid=data["candidat"])
        if candidat.count() == 1:
            candidat = candidat[0]

            uid_ref = self.generateUID() + "-" + self.generateUID()
            person = Person()
            person.name = data["name"]
            person.email = data["email"]
            person.phone = data["phone"]
            person.uid = self.generateUID()
            person.uid_ref = uid_ref
            person.accept_reglement = True

            person.save()

            vote = Vote()
            vote.candidat = candidat
            vote.person = person
            vote.uid = self.generateUID()
            vote.project = candidat.project

            vote.save()

            candidat.total_votes = candidat.total_votes + 1
            candidat.save()
        else:
            status = "error"
            message = "Candidat n'existe plus, Merci de réessayer plus tard"


        return Response({ "status" : status, "message" : message, "uid_ref" : uid_ref}, content_type="application/json", status=200)

