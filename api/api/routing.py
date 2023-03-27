from django.urls import path, re_path

from consumers import ChatClientConsumer, ChatFreeConsumer
from home_app import consumers

websocket_urlpatterns = [
    path('ws/notifications/', consumers.NotificationConsumer.as_asgi()),
    path('ws/notificationsfree/', consumers.NotificationConsumerFree.as_asgi()),
    re_path(r'^ws_client/(?P<room_name>[^/]+)/$', ChatClientConsumer.as_asgi()),
    re_path(r'^ws_free/(?P<room_name>[^/]+)/$', ChatFreeConsumer.as_asgi())
]