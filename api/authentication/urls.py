
from authentication.views import *

from django.contrib import admin
from django.urls import path

from .views import verfy_email, registerUserSerialzer, signup_freeLancer, resetPasswordView, \
    emailResetPassword, addExperinece, addServices, addJobTitle, addSkills

urlpatterns = [
    path('signup_freelancer/',signup_freeLancer,name='signup_freelancer'),

    path('register/',registerUserSerialzer,name='register'),

    path('activate/',verfy_email, name='activate'),
    path('activate/',
         verfy_email, name='activate'),
    path('reset_password/', resetPasswordView, name='reset_password'),
    path('email_reset_password/', emailResetPassword, name='email_reset_password'),
    path('addExperience/',addExperinece, name='addExperinece'),
    path('addService/',addServices,name='addService'),
    path('jobTitle/',addJobTitle,name='jobTitle'),
    path('addSkills/',addSkills,name="addSkills"),
 ]
