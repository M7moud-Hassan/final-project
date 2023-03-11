
from authentication.views import *

from django.contrib import admin
from django.urls import path

<<<<<<< HEAD

from .views import *
urlpatterns = [
    path('signup_freelancer/',signup_freeLancer,name='signup_freelancer'),
    path('activate/',verfy_email, name='activate'),

]
=======
urlpatterns = [
    path('signup_freelancer/',signup_freeLancer,name='signup_freelancer'),

    path('register/',registerUserSerialzer,name='register'),

    path('activate/',verfy_email, name='activate'),
    path('activate/',
         verfy_email, name='activate'),
    path('reset_password/', resetPasswordView, name='reset_password'),
    path('email_reset_password/', emailResetPassword, name='email_reset_password'),
 ]
>>>>>>> 670acac9a8c3f3acaf3fa1a75ededd29389c0c95
