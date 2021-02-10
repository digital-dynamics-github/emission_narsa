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
    path('save-jury/', views.SaveJury.as_view(), name="save_jury"),
    path('save-block-text/', views.SaveBlockText.as_view(), name="save_block_text"),

    path('get-block-text/<str:uid>/', views.GetBlockText.as_view(), name="get_block_text"),
    path('get-reglement/<str:uid>/', views.GetReglement.as_view(), name="get_reglement"),
    path('get-candidat/<str:uid>/', views.GetCandidat.as_view(), name="get_candidat"),
    path('get-jury/<str:uid>/', views.GetJury.as_view(), name="getjury"),
    path('get-stream/<str:uid>/', views.GetStream.as_view(), name="get_stream"),



    path('update-reglement/<str:uid>/', views.UpdateReglement.as_view(), name="update_reglement"),
    path('update-candidat/<str:uid>/', views.UpdateCandidat.as_view(), name="update_candidat"),
    path('update-jury/<str:uid>/', views.UpdateJury.as_view(), name="update_jury"),
    path('update-stream/<str:uid>/', views.UpdateStream.as_view(), name="update_stream"),
    path('update-block-text/<str:uid>/', views.UpdateBlockText.as_view(), name="update_block_text"),


    path('delete-element/<str:element>/<str:uid>/', views.DeleteElement.as_view(), name="delete_stream"),

]



