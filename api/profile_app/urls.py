from django.urls import path

from .views import  *

urlpatterns = [
    path('get_all_certificatins/', get_all_certificatins_serializer, name='get_all_certificatins_serializer'),
    path('get_Portfilo_using_id/', get_Portfilo_using_id_serializer, name='get_Portfilo_using_id_serializer'),
    path('add_portfilo/', add_portflio, name='add_portfilo'),
    path('add_certification/', add_certification, name='add_certification'),
    path('get_all_certificatins/', get_all_certificatins_serializer, name='get_all_certificatins_serializer'),
    path("get_details_free/",details_freelancer),
    path('get_payment_using_id/', get_payment_using_id_serializer, name='get_payment_using_id_serializer'),
    path("add_payment/", add_payment, name='add_payment'),
    path('clientDetails',clientDetails,name='clientDetails'),
    path('get_work_history_user_id/', get_work_history_user_id_serializer, name='get_work_history_user_id_serializer'),
    path("add_work_history_user/", add_work_history_user, name='add_work_history_user'),

]
