import os
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack

from django.urls import path
from django.core.asgi import get_asgi_application
os.environ.setdefault('DJANGO_SETTINGS_MODULE','api.settings')
from home_app.consumers import NotificationConsumer, NotificationConsumerFree

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter([path('ws/notifications/', NotificationConsumer.as_asgi()),
                   path('ws/notificationsfree/', NotificationConsumerFree.as_asgi())]))

})