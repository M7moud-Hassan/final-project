from django.urls import path

from .views import *
urlpatterns = [
    path('signup_freelancer/',signup_freeLancer,name='signup_freelancer'),
    path('activate/',
         verfy_email, name='activate'),
    path('reset_password/', resetPasswordView, name='reset_password'),
    path('email_reset_password/', emailResetPassword, name='email_reset_password'),
 ]