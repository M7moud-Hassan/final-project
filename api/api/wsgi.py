import os
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack

from django.urls import path, re_path
from django.core.asgi import get_asgi_application

from chat_app.consumers import ChatClientConsumer, ChatFreeConsumer

os.environ.setdefault('DJANGO_SETTINGS_MODULE','api.settings')
from home_app.consumers import NotificationConsumer, NotificationConsumerFree

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter([path('ws/notifications/', NotificationConsumer.as_asgi()),
                   path('ws/notificationsfree/', NotificationConsumerFree.as_asgi()),
                   path('ws/chatClient/', ChatClientConsumer.as_asgi()),
                    re_path(r'^ws_client/(?P<room_name>[^/]+)/$', ChatClientConsumer.as_asgi()),
                   re_path(r'^ws_free/(?P<room_name>[^/]+)/$', ChatFreeConsumer.as_asgi())
                   ]))

})