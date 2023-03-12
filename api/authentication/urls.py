
from authentication.views import *

from django.contrib import admin
from django.urls import path


from .views import *

urlpatterns = [
    path('signup_freelancer/',signup_freeLancer,name='signup_freelancer'),
    path('reset_password/<uidb64>/<token>/', resetPasswordView, name='reset_password'),
    path('email_reset_password/', emailResetPassword, name='email_reset_password'),
    path('register/',registerUserSerialzer,name='register'),
    path('activate/',verfy_email, name='activate'),
    path('reset_password/', resetPasswordView, name='reset_password'),
    path('view_service/', view_service_serializer, name='view_service_serializer'),
    path('view_skills/', view_skills_serializer, name='view_skills_serializer'),
 ]

