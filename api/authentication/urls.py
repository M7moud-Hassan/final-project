
from .views import *

from django.contrib import admin
from django.urls import path

from .views import  *

urlpatterns = [
    path('signup_freelancer/',signup_freeLancer,name='signup_freelancer'),
    path('register/',registerUserSerialzer,name='register'),
    path('rest_password_check/', reset_password_View),
    path('rest_password_view_user/', rest_password_view_user, name='reset_password_free'),

    path('addExperience/',addExperinece, name='addExperinece'),
    path('addService/',addServices,name='addService'),
    path('jobTitle/',addJobTitle,name='jobTitle'),
    path('addSkills/',addSkills,name="addSkills"),
    path('set_password/',set_password,name="set_password"),
    path('activate_free/',verfy_email_free, name='activate'),
    path('email_reset_password/', emailResetPassword, name='email_reset_password'),
    path('save_education/', save_education, name='save_education'),
    path('save_overview/', save_overview, name='save_overview'),
    path('login/', login, name='save_overview'),
    path('get_skills/',view_skills_serializer),
    path('get_Services/', view_service_serializer),
    path('activate_user_email/',verfy_email_register),
    path('check_email/',check_email),
    path('view_category_services/',view_category_services_serializer,name='view_category_services_serializer'),
    path('get_all_certification_type/',get_all_certification_type_serializer,name='get_all_certification_type_serializer'),
    path('get_all_certificatins/',get_all_certificatins_serializer,name='get_all_certificatins_serializer'),
    path('get_certificatins_using/<int:pk>/',get_certificatins_using_id_serializer,name='get_certificatins_using_id_serializer'),
    path('add_portfilo/',add_portfilo,name='add_portfilo'),
    path('add_certification/',add_certification,name='add_certification'),
 ]

