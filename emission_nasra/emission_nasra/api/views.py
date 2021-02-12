# -*- coding: utf-8 -*-

from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework.permissions import AllowAny, IsAuthenticated

from emission_nasra.template_api_view_custom import TemplateAPIViewCustom
from stream.models import Stream, BlockText
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
        stream.title = data["title_ar"]
        stream.description = data["description_ar"]
        stream.code = data["code"]
        stream.code_ar = data["code_ar"]
        stream.uid = self.generateUID()

        streams_active = Stream.objects.all().filter(active=True)
        if streams_active.count() > 0:
            for str_act in streams_active:
                str_act.active = False
                str_act.save()

        stream.active = True
        stream.save()


        return Response({ "status" : status, "message" : message, }, content_type="application/json", status=200)

class UpdateStream(TemplateAPIViewCustom):
    permission_classes = (AllowAny,)
    renderer_classes = (JSONRenderer,)
    limit_per_page = 10

    def post(self, request, uid):
        message = "تمت العملية بنجاح"
        status = "success"

        data = request.data

        stream = Stream.objects.all().filter(uid=uid)
        if stream.count() == 1:
            stream = stream[0]
            stream.title = data["title"]
            stream.description = data["description"]
            stream.title_ar = data["title_ar"]
            stream.description_ar = data["description_ar"]
            stream.code = data["code"]
            stream.code_ar = data["code_ar"]

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
        reglement.title_ar = data["title_ar"]
        reglement.content_ar = data["content_ar"]
        reglement.save()


        return Response({ "status" : status, "message" : message, }, content_type="application/json", status=200)

class SaveBlockText(TemplateAPIViewCustom):
    permission_classes = (AllowAny,)
    renderer_classes = (JSONRenderer,)
    limit_per_page = 10

    def post(self, request):
        message = "تمت العملية بنجاح"
        status = "success"

        data = request.data

        element = BlockText()
        element.title = data["title"]
        element.description = data["description"]
        element.title_ar = data["title_ar"]
        element.description_ar = data["description_ar"]
        element.location = data["location"]
        element.save()


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
            reglement.title_ar = data["title_ar"]
            reglement.content_ar = data["content_ar"]
            reglement.save()


        return Response({ "status" : status, "message" : message, }, content_type="application/json", status=200)

class UpdateBlockText(TemplateAPIViewCustom):
    permission_classes = (AllowAny,)
    renderer_classes = (JSONRenderer,)
    limit_per_page = 10

    def post(self, request, uid):
        message = "تمت العملية بنجاح"
        status = "success"

        data = request.data

        element = BlockText.objects.all().filter(uid=uid)
        if element.count() == 1:
            element = element[0]
            element.title = data["title"]
            element.description = data["description"]
            element.title_ar = data["title_ar"]
            element.description_ar = data["description_ar"]
            element.location = data["location"]
            element.save()


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
            data = { "title" : reglement.title, "content" : reglement.content, "title_ar" : reglement.title_ar, "content_ar" : reglement.content_ar }



        return Response({ "status" : status, "message" : message, "data" : data }, content_type="application/json", status=200)

class GetBlockText(TemplateAPIViewCustom):
    permission_classes = (AllowAny,)
    renderer_classes = (JSONRenderer,)
    limit_per_page = 10

    def get(self, request, uid):
        message = "تمت العملية بنجاح"
        status = "success"

        data = None

        block_text = BlockText.objects.all().filter(uid=uid)
        if block_text.count() == 1:
            block_text = block_text[0]
            data = { "title" : block_text.title, "description" : block_text.description, 'title_ar' : block_text.title_ar, "description_ar" : block_text.description_ar, "location" : block_text.location }



        return Response({ "status" : status, "message" : message, "data" : data }, content_type="application/json", status=200)

class GetCandidat(TemplateAPIViewCustom):
    permission_classes = (AllowAny,)
    renderer_classes = (JSONRenderer,)
    limit_per_page = 10

    def get(self, request, uid):
        message = "تمت العملية بنجاح"
        status = "success"

        data = None

        candidat = Candidat.objects.all().filter(uid=uid)
        if candidat.count() == 1:
            candidat = candidat[0]
            data = {
                "title_project" : candidat.project.title,
                "second_title_project" : candidat.project.second_title,
                "content_project" : candidat.project.content,
                "video_project" : candidat.project.video,
                "title_project_ar" : candidat.project.title_ar,
                "second_title_project_ar" : candidat.project.second_title_ar,
                "content_project_ar" : candidat.project.content_ar,
                "category_project_" : candidat.project.category,
                "category_project_ar" : candidat.project.category_ar,
                "first_name" : candidat.first_name,
                "last_name" : candidat.last_name,
                "first_name_ar" : candidat.first_name_ar,
                "last_name_ar" : candidat.last_name_ar,
                "email" : candidat.email,
                "site_web" : candidat.site_web,
                "facebook" : candidat.facebook,
                "twitter" : candidat.twitter,
                "about" : candidat.about,
                "about_ar" : candidat.about_ar,
                "position" : candidat.position,
                "position_ar" : candidat.position_ar,
                "company" : candidat.company,
                "company_ar" : candidat.company_ar,
            }



        return Response({ "status" : status, "message" : message, "data" : data }, content_type="application/json", status=200)

class GetJury(TemplateAPIViewCustom):
    permission_classes = (AllowAny,)
    renderer_classes = (JSONRenderer,)
    limit_per_page = 10

    def get(self, request, uid):
        message = "تمت العملية بنجاح"
        status = "success"

        data = None

        jury = Jury.objects.all().filter(uid=uid)
        if jury.count() == 1:
            jury = jury[0]
            data = {
                "first_name" : jury.first_name,
                "last_name" : jury.last_name,
                "first_name_ar" : jury.first_name_ar,
                "last_name_ar" : jury.last_name_ar,
                "email" : jury.email,
                "site_web" : jury.site_web,
                "facebook" : jury.facebook,
                "twitter" : jury.twitter,
                "about" : jury.about,
                "about_ar" : jury.about_ar,
                "position" : jury.position,
                "position_ar" : jury.position_ar,
                "company" : jury.company,
                "company_ar" : jury.company_ar,
            }



        return Response({ "status" : status, "message" : message, "data" : data }, content_type="application/json", status=200)


class GetStream(TemplateAPIViewCustom):
    permission_classes = (AllowAny,)
    renderer_classes = (JSONRenderer,)
    limit_per_page = 10

    def get(self, request, uid):
        message = "تمت العملية بنجاح"
        status = "success"

        data = None

        stream = Stream.objects.all().filter(uid=uid)
        if stream.count() == 1:
            stream = stream[0]
            data = {
                "title" : stream.title,
                "description" : stream.description,
                "title_ar" : stream.title_ar,
                "description_ar" : stream.description_ar,
                "code" : stream.code,
                "code_ar" : stream.code_ar,
            }



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
        project.title_ar = data["title_project_ar"]
        project.second_title_ar = data["second_title_project_ar"]
        project.content_ar = data["content_project_ar"]
        project.video = data["video_project"]
        project.category = data["category_project"]
        project.category_ar = data["category_project_ar"]

        project.uid = self.generateUID()

        project.save()


        candidat = Candidat()
        candidat.project = project
        candidat.first_name = data["first_name"]
        candidat.last_name = data["last_name"]
        candidat.first_name_ar = data["first_name_ar"]
        candidat.last_name_ar = data["last_name_ar"]
        candidat.email = data["email"]
        candidat.site_web = data["site_web"]
        candidat.facebook = data["facebook"]
        candidat.twitter = data["twitter"]
        candidat.position = data["position"]
        candidat.company = data["company"]
        candidat.about = data["about"]

        candidat.position_ar = data["position_ar"]
        candidat.company_ar = data["company_ar"]
        candidat.about_ar = data["about_ar"]

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

class UpdateCandidat(TemplateAPIViewCustom):
    permission_classes = (AllowAny,)
    renderer_classes = (JSONRenderer,)
    limit_per_page = 10

    def post(self, request, uid):
        message = "تمت العملية بنجاح"
        status = "success"

        data = request.data

        candidat  = Candidat.objects.all().filter(uid=uid)
        if candidat.count() == 1 :
            candidat = candidat[0]

            project = candidat.project
            project.title = data["title_project"]
            project.second_title = data["second_title_project"]
            project.content = data["content_project"]
            project.title_ar = data["title_project_ar"]
            project.second_title_ar = data["second_title_project_ar"]
            project.content_ar = data["content_project_ar"]
            project.category = data["category_project"]
            project.category_ar = data["category_project_ar"]
            project.video = data["video_project"]

            project.save()

            candidat.project = project
            candidat.first_name = data["first_name"]
            candidat.last_name = data["last_name"]
            candidat.first_name_ar = data["first_name_ar"]
            candidat.last_name_ar = data["last_name_ar"]
            candidat.email = data["email"]
            candidat.site_web = data["site_web"]
            candidat.facebook = data["facebook"]
            candidat.twitter = data["twitter"]
            candidat.position = data["position"]
            candidat.company = data["company"]
            candidat.about = data["about"]

            candidat.position_ar = data["position_ar"]
            candidat.company_ar = data["company_ar"]
            candidat.about_ar = data["about_ar"]

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

class SaveJury(TemplateAPIViewCustom):
    permission_classes = (AllowAny,)
    renderer_classes = (JSONRenderer,)
    limit_per_page = 10

    def post(self, request):
        message = "تمت العملية بنجاح"
        status = "success"

        data = request.data

        jury = Jury()
        jury.first_name = data["first_name"]
        jury.first_name_ar = data["first_name_ar"]
        jury.last_name = data["last_name"]
        jury.last_name_ar = data["last_name_ar"]
        jury.email = data["email"]
        jury.site_web = data["site_web"]
        jury.facebook = data["facebook"]
        jury.twitter = data["twitter"]
        jury.position = data["position"]
        jury.position_ar = data["position_ar"]
        jury.company = data["company"]
        jury.company_ar = data["company_ar"]
        jury.about = data["company"]
        jury.about_ar = data["about_ar"]
        jury.uid = self.generateUID()

        photo_base_64 = data["photo_base64"]

        if not photo_base_64 == "" and not photo_base_64 == "photo":
            format, imgstr = photo_base_64.split(';base64,')
            ext = format.split('/')[-1]
            file_name = str(jury.uid) + "." + ext
            try:
                os.remove(jury.photo.path)
            except:
                a = ""

        if not photo_base_64 == "" and not photo_base_64 == "photo":
            format, imgstr = photo_base_64.split(';base64,')
            ext = format.split('/')[-1]
            data_file = ContentFile(base64.b64decode(imgstr))
            file_name = str(jury.uid) + "." + ext
            jury.photo.save(file_name, data_file, save=True)




        jury.save()


        return Response({ "status" : status, "message" : message, }, content_type="application/json", status=200)

class UpdateJury(TemplateAPIViewCustom):
    permission_classes = (AllowAny,)
    renderer_classes = (JSONRenderer,)
    limit_per_page = 10

    def post(self, request, uid):
        message = "تمت العملية بنجاح"
        status = "success"

        data = request.data
        jury = Jury.objects.all().filter(uid=uid)
        if jury.count() == 1 :
            jury = jury[0]
            jury.first_name = data["first_name"]
            jury.first_name_ar = data["first_name_ar"]
            jury.last_name = data["last_name"]
            jury.last_name_ar = data["last_name_ar"]
            jury.email = data["email"]
            jury.site_web = data["site_web"]
            jury.facebook = data["facebook"]
            jury.twitter = data["twitter"]
            jury.position = data["position"]
            jury.position_ar = data["position_ar"]
            jury.company = data["company"]
            jury.company_ar = data["company_ar"]
            jury.about = data["company"]
            jury.about_ar = data["about_ar"]

            photo_base_64 = data["photo_base64"]

            if not photo_base_64 == "" and not photo_base_64 == "photo":
                format, imgstr = photo_base_64.split(';base64,')
                ext = format.split('/')[-1]
                file_name = str(jury.uid) + "." + ext
                try:
                    os.remove(jury.photo.path)
                except:
                    a = ""

            if not photo_base_64 == "" and not photo_base_64 == "photo":
                format, imgstr = photo_base_64.split(';base64,')
                ext = format.split('/')[-1]
                data_file = ContentFile(base64.b64decode(imgstr))
                file_name = str(jury.uid) + "." + ext
                jury.photo.save(file_name, data_file, save=True)



            jury.save()


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
        config_vote = Config.objects.all().filter(type="vote", active=True)
        if candidat.count() == 1 and config_vote.count() > 0:
            candidat = candidat[0]

            config_demo = Config.objects.all().filter(type="demo", active=True)
            site_demo = False
            if config_demo.count() == 1:
                site_demo = True


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


        return Response({ "status" : status, "message" : message, "uid_ref" : uid_ref, "site_demo" : site_demo}, content_type="application/json", status=200)

class DeleteElement(TemplateAPIViewCustom):
    permission_classes = (AllowAny,)
    renderer_classes = (JSONRenderer,)
    limit_per_page = 10

    def get(self, request, element, uid):
        message = "merci pour votre vote"
        status = "success"

        element_object = None
        if element == "stream":
            element_object = Stream.objects.all().filter(uid=uid)

        if element == "candidat":
            element_object = Candidat.objects.all().filter(uid=uid)

        if element == "jury":
            element_object = Jury.objects.all().filter(uid=uid)

        if element == "reglement":
            element_object = Reglement.objects.all().filter(uid=uid)

        if not element_object == None:
            element_object.delete()

        return Response({ "status" : status, "message" : message,}, content_type="application/json", status=200)

