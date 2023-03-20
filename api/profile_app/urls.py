from django.urls import path

from .views import  *

urlpatterns = [
    path('get_all_certificatins/', get_all_certificatins_serializer, name='get_all_certificatins_serializer'),
    path('get_certificatins_using_id/', get_Portfilo_using_id_serializer, name='get_certificatins_using_id_serializer'),
    path('add_portfilo/', add_portflio, name='add_portfilo'),
    path('add_certification/', add_certification, name='add_certification'),
    path("get_details_free/",details_freelancer),
    path('clientDetails/',clientDetails,name='clientDetails'),
    path('updateSkills/',updateSkills),
    path('updateservices/',updateServices),
    path('delete_experience/',delete_experience),
    path('getExperience/',getExperience),
    path('secondaryDetails/', secondaryDetails, name='secondary_details'),
    path('updateImageUser/',updateImageUser),
    path('getalltypesCertifications/',get_all_certification_type_serializer),
    path('add_history_employment/',add_history_employment),
    path('delEducation/',delEducation),
    path('delPortFilo/',delPortFilo),
    path('delcertificate/',delcertificate),
    path('delHistoryEmpl/',delHistoryEmpl)
]
