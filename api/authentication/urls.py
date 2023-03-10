from django.urls import path


from .views import *
urlpatterns = [
    path('signup_freelancer/',signup_freeLancer,name='signup_freelancer'),
    path('activate/',verfy_email, name='activate'),

]