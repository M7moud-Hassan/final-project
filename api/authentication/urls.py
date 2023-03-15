
from .views import *

from django.contrib import admin
from django.urls import path

from .views import  registerUserSerialzer, signup_freeLancer, resetPasswordView, \
    emailResetPassword, addExperinece, addServices, addJobTitle, addSkills

urlpatterns = [
    path('signup_freelancer/',signup_freeLancer,name='signup_freelancer'),
    path('register/',registerUserSerialzer,name='register'),
    path('reset_password/', resetPasswordView, name='reset_password'),
    path('email_reset_password/', emailResetPassword, name='email_reset_password'),
    path('addExperience/',addExperinece, name='addExperinece'),
    path('addService/',addServices,name='addService'),
    path('jobTitle/',addJobTitle,name='jobTitle'),
    path('addSkills/',addSkills,name="addSkills"),
    path('activate/',verfy_email_free, name='activate'),
    path('activateuser/',verify_email_register, name='activateuser'),
    path('reset_password/', resetPasswordView, name='reset_password'),
    path('email_reset_password/', emailResetPassword, name='email_reset_password'),
    path('save_education/', save_education, name='save_education'),
    path('save_overview/', save_overview, name='save_overview'),
    path('login/', login, name='save_overview'),

 ]

