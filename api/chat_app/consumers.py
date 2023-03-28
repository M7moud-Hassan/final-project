from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from channels.layers import get_channel_layer
from django.contrib.auth.models import AnonymousUser
from rest_framework.utils import json

from chat_app.models import ChatMessageClient, ChatMessage, ChatMessageFree
from chat_app.serializers import ChatMessageClientSerializer, ChatMessageFreeSerializer, ChatMessageSerializer
from authentication.models import RegisterFreelancer, RegisterUser


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
def create_message_client(client, free, mess):
    chat = ChatMessageClient.objects.filter(sender=client, receiver=free).first()
    msg=None
    if chat:
        msg=ChatMessage.objects.create(message=mess,client=True)
        chat.messages.add(msg)
    else:
        chat = ChatMessageClient.objects.create(sender=client, receiver=free)
        msg=ChatMessage.objects.create(message=mess,client=True)
        chat.messages.add(msg)
    return (ChatMessageSerializer(msg).data,client.id)


@database_sync_to_async
def create_message_free(free, client, mess):
    chat = ChatMessageFree.objects.filter(sender=free, receiver=client).first()
    msg = None
    if chat:
        msg=ChatMessage.objects.create(message=mess,free=True)
        chat.messages.add(msg)
    else:
        chat = ChatMessageFree.objects.create(sender=free, receiver=client)
        msg=ChatMessage.objects.create(message=mess,free=True)
        chat.messages.add(msg)
    return (ChatMessageSerializer(msg).data,free.id)


class ChatClientConsumer(AsyncWebsocketConsumer):
    async def websocket_connect(self, event):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name
        await self.channel_layer.group_add(self.room_group_name, self.channel_name)
        await self.accept()

    async def websocket_receive(self, event):
        sen = json.loads(event['text'])
        free = await get_free(sen['free'])
        client = await get_client(sen['client'])
        mes = await create_message_client(client,free, sen['message'])
        channel_layer = get_channel_layer()
        await (channel_layer.group_send)(
            'chat_%s' % sen['room'],
            {
                "type": "send_chat",
                "value": json.dumps(mes)
            })

    async def websocket_disconnect(self, event):
        print('disconnect', event)

    async def send_chat(self, event):
        await self.send(json.dumps({
            "type": "websocket.send",
            "data": event
        }))


class ChatFreeConsumer(AsyncWebsocketConsumer):
    async def websocket_connect(self, event):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name

        await self.channel_layer.group_add(self.room_group_name, self.channel_name)
        await self.accept()

    async def websocket_receive(self, event):

        sen = json.loads(event['text'])
        free = await get_free(sen['free'])
        client = await get_client(sen['client'])
        mes = await create_message_free(free,client, sen['message'])
        channel_layer = get_channel_layer()
        await (channel_layer.group_send)(
            'chat_%s' % sen['room'],
            {
                "type": "send_chat",
                "value": json.dumps(mes)
            })

    async def websocket_disconnect(self, event):
        print('disconnect', event)

    async def send_chat(self, event):
        await self.send(json.dumps({
            "type": "websocket.send",
            "data": event
        }))
