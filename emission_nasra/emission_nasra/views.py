#-*- coding: utf-8 -*-

from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from stream.models import Stream, BlockText
from candidat.models import Candidat, Project
from config.models import Config
from contact.models import Person
from vote.models import Vote, Reglement
from django.http import HttpResponse
from jury.models import Jury
import xlwt

from .forms import LoginForm, ContactForm
from django.contrib.auth import authenticate, login, logout

from contact.models import Contact


class LoginAdministrator(TemplateView):
    http_method_names = ['get', "post" ]
    template_name = 'login_administrator.html'
    next_page = ""
    def get(self, request):
        form = LoginForm
        if request.user.is_authenticated:
            redirect("/interface-administrator/")



        return render(request, self.template_name, {"form": form})


    def getAttribute(self, label, data):
        return data[label]

    def post(self, request):
        form = LoginForm(request.POST)
        message = ''

        if form.is_valid():
            data = form.cleaned_data
            username = self.getAttribute("username", data)
            password = self.getAttribute("password", data)

            user = authenticate(username=username, password=password)

            if user:
                login(request, user)
                return redirect('/interface-administrator/')

        return render(request, self.template_name, {"form": form, "message": message})


class LogoutAdministrator(TemplateView):
    template_name = "blank.html"
    login = False

    def get(self, request):
        logout(request)
        return HttpResponseRedirect('/login-administrator/')

class InterfaceAdministrator(TemplateView):
    http_method_names = ['get', ]
    template_name = 'interface_administrator.html'


    def get(self, request):

        if request.user.is_anonymous == True:
            return redirect("/login-administrator/")

        streams = Stream.objects.all().order_by("-id")

        candidats = Candidat.objects.all().order_by("-total_votes")
        jurys = Jury.objects.all().order_by("-id")

        config = Config.objects.all().filter(type="vote")
        if config.count() == 1 :
            config = config[0]
        else:
            config = None

        config_demo = Config.objects.all().filter(type="demo", active=True)
        if config_demo.count() == 1 :
            config_demo = config_demo[0]
        else:
            config_demo = None

        reglement = None
        regelement_object = Reglement.objects.all()
        if regelement_object.count() > 0 :
            reglement = regelement_object[0]

        block_text = None
        block_text_object = BlockText.objects.all().filter(location="home")
        if block_text_object.count() > 0:
            block_text = block_text_object[0]

        block_script = None
        block_script_object = BlockText.objects.all().filter(location="script")
        if block_script_object.count() > 0:
            block_script = block_script_object[0]




        return render(request, self.template_name, { "streams" : streams, "candidats" : candidats, "config_vote" : config, "reglement" : reglement, "jurys" : jurys, "block_text" : block_text, "block_script" : block_script, "config_demo" : config_demo})

class HomePage(TemplateView):
    http_method_names = ['get', ]
    template_name = 'home_page.html'

    def get(self, request):
        request.get_path_page = request.get_full_path().replace("/ar/", "").replace("/fr/", "")

        config_vote = Config.objects.all().filter(type="vote", active=True)
        accept_vote = False
        if config_vote.count() > 0:
            accept_vote = True


        stream = Stream.objects.all().filter(active=True)
        stream_object = None
        if stream.count() == 1:
            stream_object = stream[0]

        candidats = Candidat.objects.all().order_by("-id")

        config_jauge = Config.objects.all().filter(type="jauge_candidat", active=True)

        display_jauge_candidat = False

        if config_jauge.count() == 1 :
            display_jauge_candidat = True

        total_votes_global = Vote.objects.all().count()

        for cand in candidats:
            cand.pourcent_votes = (float(cand.total_votes) * 100) /  float(total_votes_global)
            cand.pourcent_votes = round(float(cand.pourcent_votes), 2)
            cand.pourcent_votes_string = str(cand.pourcent_votes).replace(",", ".")




        jurys = Jury.objects.all().order_by("-id")

        block_text_home = BlockText.objects.all().filter(location="home").order_by("-id")
        text_home = None
        if block_text_home.count() > 0 :
            text_home = block_text_home[0]

        block_script = BlockText.objects.all().filter(location="script").order_by("-id")
        script_site = None
        if block_script.count() > 0:
            script_site = block_script[0]

        return render(request, self.template_name, {  "candidats" : candidats, "jurys" : jurys, "text_home" : text_home, "script_site" : script_site, "stream_object" : stream_object,
                                                      "display_jauge_candidat" : display_jauge_candidat, "accept_vote" : accept_vote

                                                      })

class CandidatsPage(TemplateView):
    http_method_names = ['get', ]
    template_name = 'candidats_page.html'

    def get(self, request):
        request.get_path_page = request.get_full_path().replace("/ar/", "").replace("/fr/", "")

        config_vote = Config.objects.all().filter(type="vote", active=True)
        accept_vote = False
        if config_vote.count() > 0:
            accept_vote = True

        candidats = Candidat.objects.all().order_by("-id")

        config_jauge = Config.objects.all().filter(type="jauge_candidat", active=True)

        display_jauge_candidat = False

        if config_jauge.count() == 1:
            display_jauge_candidat = True

        total_votes_global = Vote.objects.all().count()

        for cand in candidats:
            cand.pourcent_votes = (float(cand.total_votes) * 100) / float(total_votes_global)
            cand.pourcent_votes = round(float(cand.pourcent_votes), 2)
            cand.pourcent_votes_string = str(cand.pourcent_votes).replace(",", ".")

        stream = Stream.objects.all().filter(active=True)
        stream_object = None
        if stream.count() == 1:
            stream_object = stream[0]


        block_script = BlockText.objects.all().filter(location="script").order_by("-id")
        script_site = None
        if block_script.count() > 0:
            script_site = block_script[0]

        return render(request, self.template_name, {  "candidats" : candidats, "script_site" : script_site, "stream_object" : stream_object,
                                                      "display_jauge_candidat" : display_jauge_candidat, "accept_vote" : accept_vote })

class ContactPage(TemplateView):
    http_method_names = ['get', 'post']
    template_name = 'contact.html'


    def get(self, request):
        form = ContactForm

        request.get_path_page = request.get_full_path().replace("/ar/", "").replace("/fr/", "")

        block_script = BlockText.objects.all().filter(location="script").order_by("-id")
        script_site = None
        if block_script.count() > 0:
            script_site = block_script[0]

        return render(request, self.template_name, {"form": form, "script_site" : script_site})

    def post(self, request):
        form = ContactForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            name = data["name"]

            email = data["email"]
            message = data["message"]
            contact = Contact()
            contact.name = name
            contact.email = email
            contact.message = message
            contact.save()
            return HttpResponseRedirect('/merci/')
        else:

            block_script = BlockText.objects.all().filter(location="script").order_by("-id")
            script_site = None
            if block_script.count() > 0:
                script_site = block_script[0]

            return render(request, self.template_name, {"form": form, "message" : "merci de corriger les erreurs suivants", "script_site" : script_site })

class MerciPage(TemplateView):
    http_method_names = ['get', 'post']
    template_name = 'thank_you.html'



    def get(self, request):
        request.get_path_page = request.get_full_path().replace("/ar/", "").replace("/fr/", "")

        block_script = BlockText.objects.all().filter(location="script").order_by("-id")
        script_site = None
        if block_script.count() > 0:
            script_site = block_script[0]

        return render(request, self.template_name, { "script_site" : script_site })

class JuryPage(TemplateView):
    http_method_names = ['get', ]
    template_name = 'jury_page.html'

    def get(self, request):
        request.get_path_page = request.get_full_path().replace("/ar/", "").replace("/fr/", "")

        jurys = Jury.objects.all().order_by("-id")

        stream = Stream.objects.all().filter(active=True)
        stream_object = None
        if stream.count() == 1:
            stream_object = stream[0]

        block_script = BlockText.objects.all().filter(location="script").order_by("-id")
        script_site = None
        if block_script.count() > 0:
            script_site = block_script[0]

        return render(request, self.template_name, {  "jurys" : jurys, "script_site" : script_site, "stream_object" : stream_object })

class ExportCandidat(TemplateView):
    http_method_names = ['get', ]
    template_name = 'blank.html'

    def get(self, request):

        response = HttpResponse(content_type='application/ms-excel')
        response['Content-Disposition'] = 'attachment; filename="export_users.xls"'

        wb = xlwt.Workbook(encoding='utf-8')
        ws = wb.add_sheet('Users')

        # Sheet header, first row
        row_num = 0

        font_style = xlwt.XFStyle()
        font_style.font.bold = True

        columns = ['Nom complet', 'Adresse email', 'Numéro de téléphone', ]

        for col_num in range(len(columns)):
            ws.write(row_num, col_num, columns[col_num], font_style)

        # Sheet body, remaining rows
        font_style = xlwt.XFStyle()

        rows = Person.objects.all().values_list('name', 'email', 'phone')
        for row in rows:
            row_num += 1
            for col_num in range(len(row)):
                ws.write(row_num, col_num, row[col_num], font_style)

        wb.save(response)
        return response

        #return render(request, self.template_name, {  {}})

class DetailsCandidat(TemplateView):
    http_method_names = ['get', ]
    template_name = 'details_candidat.html'

    def get(self, request, uid):
        request.get_path_page = request.get_full_path().replace("/ar/", "").replace("/fr/", "")
        candidat = Candidat.objects.all().filter(uid=uid)
        if candidat.count() == 1 :
            candidat = candidat[0]

            stream = Stream.objects.all().filter(active=True)
            stream_object = None
            if stream.count() == 1:
                stream_object = stream[0]


            block_script = BlockText.objects.all().filter(location="script").order_by("-id")
            script_site = None
            if block_script.count() > 0:
                script_site = block_script[0]

            return render(request, self.template_name, { "candidat" : candidat, "script_site" : script_site, "stream_object" : stream_object })
        else:
            return redirect("/")

class ReglementsPage(TemplateView):
    http_method_names = ['get', ]
    template_name = 'reglement_page.html'

    def get(self, request):

        request.get_path_page = request.get_full_path().replace("/ar/", "").replace("/fr/", "")
        reglement = Reglement.objects.all().order_by("-id")
        if reglement.count() > 0 :
            reglement =  reglement[0]
        else:
            return redirect("/")

        block_script = BlockText.objects.all().filter(location="script").order_by("-id")
        script_site = None
        if block_script.count() > 0:
            script_site = block_script[0]

        return render(request, self.template_name, { "content" : reglement.content, "title" : reglement.title, "title_ar" : reglement.title_ar, "content_ar" : reglement.content_ar, "script_site" : script_site })





