"""emission_nasra URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import  include, url
from django.urls import path
from . import views
import django.views
from django.conf.urls.i18n import i18n_patterns

from django.conf import settings
from django.conf.urls.static import static

'''
def trigger_error(request):
    division_by_zero = 1 / 0
'''


urlpatterns = [

    #path('sentry-debug/', trigger_error),

    path('admin/', admin.site.urls),
    path('interface-administrator/', views.InterfaceAdministrator.as_view(), name="interface_administrator"),


    path('api/site/', include(('emission_nasra.api.urls', 'site'), namespace='api_site')),


    path('logout/', views.LogoutAdministrator.as_view(), name="login_administrator"),
    path('login-administrator/', views.LoginAdministrator.as_view(), name="login_administrator"),
    path('exporter-candidat/', views.ExportCandidat.as_view(), name="export_candidat"),


    url(r'^media/(?P<path>.*)$', django.views.static.serve,{'document_root': settings.MEDIA_ROOT, 'show_indexes': True}, name='media'),

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


urlpatterns += i18n_patterns(
    path('', views.HomePage.as_view(), name="home"),
    path('jury/', views.JuryPage.as_view(), name="jury_page"),
    path('reglements/', views.ReglementsPage.as_view(), name="reglements"),
    path('contact/', views.ContactPage.as_view(), name="contact_page"),
    path('merci/', views.MerciPage.as_view(), name="merci_page"),
    path('test-live/', views.TestLive.as_view(), name="test_live"),

    path('initiative/', views.CandidatsPage.as_view(), name="candidats_page"),

    path('details-candidat/<str:uid>/', views.DetailsCandidat.as_view(), name="details_candidat"),
)