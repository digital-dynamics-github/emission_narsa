from django.conf.urls import url
from django.contrib import admin

from emission_nasra.api import views
from django.urls import path, include
urlpatterns = [
    #### get list the components


    path('active-widget/<str:type>/<str:uid>/', views.ActiveWidget.as_view(), name="active_widget"),
    path('save-stream/', views.SaveStream.as_view(), name="save_stream"),
    path('save-reglement/', views.SaveReglement.as_view(), name="save_reglement"),
    path('save-candidat/', views.SaveCandidat.as_view(), name="save_candidat"),
    path('save-person/', views.SavePerson.as_view(), name="save_person"),

    path('get-reglement/<str:uid>/', views.GetReglement.as_view(), name="get_reglement"),
    path('update-reglement/<str:uid>/', views.UpdateReglement.as_view(), name="update_reglement"),

]



