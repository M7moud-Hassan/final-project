
from .views import *

from django.contrib import admin
from django.urls import path

from .views import  *


urlpatterns = [
    path('getMessagesChatsFree/',getMessagesChatsFree),
    path('getMessagesChatsClient/',getMessagesChatsClient),
    path('active_Free/',active_Free),
    path('active_client/',active_client),
    path('de_active_Free/', de_active_Free),
    path('de_active_client/', de_active_client),
    path('getMessagesFree/',getMessagesFree),
    path('getMessagesClent/',getMessagesClent),
    path('getUnreadMessagesClient/',getUnreadMessagesClient),
    path('getUnreadMessagesFree/',getUnreadMessagesFree),
    path('checkChatBegin/',checkChatBegin)


 ]

