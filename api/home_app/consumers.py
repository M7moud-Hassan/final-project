from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from channels.layers import get_channel_layer
from django.contrib.auth.models import AnonymousUser
from rest_framework.utils import json

from home_app.models import notificationsClient
from authentication.models import RegisterUser, RegisterFreelancer
from home_app.serlializers import NotificationClientSerializer


@database_sync_to_async
def get_client(user_id):
    try:
        return RegisterUser.objects.get(id=user_id)
    except:
        return AnonymousUser() @ database_sync_to_async


@database_sync_to_async
def get_free(user_id):
    try:
        return RegisterFreelancer.objects.get(id=user_id)
    except:
        return AnonymousUser() @ database_sync_to_async


@database_sync_to_async
def create_notification(receiver, sender, typeof, status="unread"):
    notification_to_create = notificationsClient.objects.create(
        user_revoker=receiver,
        user_sender=sender,
        type_of_notification=typeof,
        status=status
    )
    return NotificationClientSerializer(notification_to_create).data


class NotificationConsumer(AsyncWebsocketConsumer):
    async def websocket_connect(self, event):
        print(self.scope)
        await self.accept()
        await self.send(json.dumps({
            "type": "websocket.send",
            "text": "connect to notifications"
        }))
        self.room_name = 'notifications'
        self.room_group_name = 'clients'
        await self.channel_layer.group_add(self.room_group_name, self.channel_name)
        self.send({
            "type": "websocket.send",
            "text": "room made"
        })

    async def websocket_receive(self, event):
        sender_ = event['sender']
        sender = await get_free(int(sender_))
        recieve=await get_client(int(event['recieve']))
        get_of = await create_notification(recieve,sender,event['payload'])
        self.room_group_name = 'clients'
        channel_layer = get_channel_layer()
        await (channel_layer.group_send)(
            self.room_group_name,
            {
                "type": "send_notification",
                "value": get_of
            })

    async def websocket_disconnect(self, event):
        print('disconnect', event)

    async def send_notification(self, event):
        await self.send(json.dumps({
            "type": "websocket.send",
            "data": event
        }))
        print('I am here')
        print(event)
