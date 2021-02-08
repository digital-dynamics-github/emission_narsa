#-*- coding: utf-8 -*-

from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from stream.models import Stream
from candidat.models import Candidat, Project
from config.models import Config
from contact.models import Person
from vote.models import Vote, Reglement
from django.http import HttpResponse
import xlwt

from .forms import LoginForm
from django.contrib.auth import authenticate, login, logout


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

        candidats = Candidat.objects.all().order_by("-id")

        config = Config.objects.all().filter(type="vote")
        if config.count() == 1 :
            config = config[0]
        else:
            config = None

        reglement = None
        regelement_object = Reglement.objects.all()
        if regelement_object.count() > 0 :
            reglement = regelement_object[0]



        return render(request, self.template_name, { "streams" : streams, "candidats" : candidats, "config_vote" : config, "reglement" : reglement })

class HomePage(TemplateView):
    http_method_names = ['get', ]
    template_name = 'home_page.html'

    def get(self, request):

        candidats = Candidat.objects.all().order_by("-id")

        return render(request, self.template_name, {  "candidats" : candidats })

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
        candidat = Candidat.objects.all().filter(uid=uid)
        if candidat.count() == 1 :
            candidat = candidat[0]

            return render(request, self.template_name, { "candidat" : candidat })
        else:
            return redirect("/")

class ReglementsPage(TemplateView):
    http_method_names = ['get', ]
    template_name = 'reglement_page.html'

    def get(self, request):
        title = "test title"
        content = "lorem ipsum content test text"

        return render(request, self.template_name, { "content" : content, "title" : title })





