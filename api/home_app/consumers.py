from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from channels.layers import get_channel_layer
from django.contrib.auth.models import AnonymousUser
from rest_framework.utils import json

from home_app.models import notificationsClient, notificationsFree
from authentication.models import RegisterUser, RegisterFreelancer
from home_app.serializers import NotificationClientSerializer, NotificationFreeSerializer


@database_sync_to_async
def get_free(user_id):
    try:
        return RegisterFreelancer.objects.get(id=user_id)
    except:
        return AnonymousUser() @ database_sync_to_async


@database_sync_to_async
def get_client(user_id):
    try:
        return RegisterUser.objects.get(id=user_id)
    except:
        return AnonymousUser() @ database_sync_to_async


@database_sync_to_async
def create_notification(user_sender, receiver, typeof="task_created", status="unread"):
    notification_to_create = notificationsClient.objects.create(status=status, user_sender=user_sender,
                                                                user_revoker=receiver, type_of_notification=typeof)
    return (NotificationClientSerializer(notification_to_create).data)


@database_sync_to_async
def create_notificationFree(user_sender, receiver, typeof="task_created", status="unread"):
    notification_to_create = notificationsFree.objects.create(status=status, user_sender=user_sender,
                                                              user_revoker=receiver, type_of_notification=typeof)
    return (NotificationFreeSerializer(notification_to_create).data)


class NotificationConsumer(AsyncWebsocketConsumer):
    async def websocket_connect(self, event):
        await self.accept()
        await self.send(json.dumps({
            "type": "websocket.send",
            "text": "hello world"
        }))
        self.room_name = 'test_consumer'
        self.room_group_name = 'test_consumer_group'
        await self.channel_layer.group_add(self.room_group_name, self.channel_name)
        self.send({
            "type": "websocket.send",
            "text": "room made"
        })

    async def websocket_receive(self, event):
        sen = json.loads(event['text'])
        print(event)
        if sen["data"]["payload"] == "off":
            self.room_group_name = 'test_consumer_group'
            channel_layer = get_channel_layer()
            await (channel_layer.group_send)(
                self.room_group_name,
                {
                    "type": "send_notification",
                    "value": json.dumps(sen["data"])
                })
        else:
            free = await get_free(int(sen['data']['sender']))
            rec = await get_client(int(sen['data']['recieve']))

            get_of = await create_notification(free, rec, f'{free} {sen["data"]["payload"]}')
            self.room_group_name = 'test_consumer_group'
            channel_layer = get_channel_layer()
            await (channel_layer.group_send)(
                self.room_group_name,
                {
                    "type": "send_notification",
                    "value": json.dumps(get_of)
                })


    async def websocket_disconnect(self, event):
        print('disconnect', event)

    async def send_notification(self, event):
        await self.send(json.dumps({
            "type": "websocket.send",
            "data": event
        }))



class NotificationConsumerFree(AsyncWebsocketConsumer):
    async def websocket_connect(self, event):
        await self.accept()
        await self.send(json.dumps({
            "type": "websocket.send",
            "text": "hello world"
        }))
        self.room_name = 'test_consumer_free'
        self.room_group_name = 'test_consumer_group_free'
        await self.channel_layer.group_add(self.room_group_name, self.channel_name)
        self.send({
            "type": "websocket.send",
            "text": "room made"
        })

    async def websocket_receive(self, event):

        sen = json.loads(event['text'])
        if sen["data"]["payload"]=="off":
            self.room_group_name = 'test_consumer_group_free'
            channel_layer = get_channel_layer()
            await (channel_layer.group_send)(
                self.room_group_name,
                {
                    "type": "send_notification",
                    "value": json.dumps(sen["data"])
                })
        else:
            free = await get_free(int(sen['data']['recieve']))
            rec = await get_client(int(sen['data']['sender']))

            get_of = await create_notificationFree(rec, free, f'{rec} {sen["data"]["payload"]}')
            self.room_group_name = 'test_consumer_group_free'
            channel_layer = get_channel_layer()
            await (channel_layer.group_send)(
                self.room_group_name,
                {
                    "type": "send_notification",
                    "value": json.dumps(get_of)
                })

    async def websocket_disconnect(self, event):
        print('disconnect', event)

    async def send_notification(self, event):
        await self.send(json.dumps({
            "type": "websocket.send",
            "data": event
        }))
