
from authentication.views import signup_freeLancer, registerUserSerialzer, verfy_email

from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('signup_freelancer/',signup_freeLancer,name='signup_freelancer'),

    path('registeru/',registerUserSerialzer,name='registeru'),

    path('activate/',verfy_email, name='activate'),
]

