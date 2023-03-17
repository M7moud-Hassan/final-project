from django.urls import path

from .views import  *

urlpatterns = [
    path('get_all_certificatins/', get_all_certificatins_serializer, name='get_all_certificatins_serializer'),
    path('get_certificatins_using_id/', get_Portfilo_using_id_serializer, name='get_certificatins_using_id_serializer'),
    path('add_portfilo/', add_portflio, name='add_portfilo'),
    path('add_certification/', add_certification, name='add_certification'),
    path('get_all_certificatins/', get_all_certificatins_serializer, name='get_all_certificatins_serializer'),

]
