
from api.authentication.views import signup_freeLancer , registerUserSerialzer

from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('', admin.site.urls),
    path('signup_freelancer/',signup_freeLancer,name='signup_freelancer'),
    path('register/',registerUserSerialzer,name='register'),
]



