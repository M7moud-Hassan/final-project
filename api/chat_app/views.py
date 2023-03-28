from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import RegisterFreelancer, RegisterUser, ChatMessageClient, ChatMessageFree
from .serializers import ChatMessageClientSerializer, FreeLancerSerializer, UserSerializer, ChatMessageFreeSerializer


# Create your views here.

@api_view(['POST'])
def getMessagesClent(request):
    free=RegisterFreelancer.objects.filter(id=request.data['free']).first()
    client = RegisterUser.objects.filter(id=request.data['client']).first()
    if free and client:
        chats =ChatMessageClient.objects.filter(receiver=free,sender=client).first()
        chats2 = ChatMessageFree.objects.filter(receiver=client, sender=free).first()
        for m in chats2.messages.all():
            m.is_read=True
            m.save()
        res=ChatMessageClientSerializer(chats).data
        res2=ChatMessageFreeSerializer(chats2).data
        messages=[]
        if res:
            for i in res['messages']:
                messages.append(i)
        if res2:
            for i in res2['messages']:
                messages.append(i)
        messages.sort(key=lambda element: element['id'])
        return Response(messages)

    else:
        return Response(status=status.HTTP_404_NOT_FOUND)
@api_view(['POST'])
def getMessagesFree(request):
    free=RegisterFreelancer.objects.filter(id=request.data['free']).first()
    client = RegisterUser.objects.filter(id=request.data['client']).first()
    if free and client:
        chats =ChatMessageFree.objects.filter(sender=free,receiver=client).first()
        chats2 = ChatMessageClient.objects.filter(receiver=free, sender=client).first()
        for m in chats2.messages.all():
            m.is_read = True
            m.save()
        res=ChatMessageFreeSerializer(chats).data
        res2=ChatMessageClientSerializer(chats2).data
        messages = []
        if res:
            for i in res['messages']:
                messages.append(i)
        if res2:
            for i in res2['messages']:
                messages.append(i)
        messages.sort(key=lambda element: element['id'])
        return Response(messages)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
def getMessagesChatsClient(request):
    client = RegisterUser.objects.filter(id=request.data['id']).first()
    if client:
        chats = ChatMessageClient.objects.filter(sender=client)
        chats2 = ChatMessageFree.objects.filter(receiver=client)
        sne=[]
        msg_read=[]
        for c in chats:
            sne.append(FreeLancerSerializer(c.receiver).data)
        for c in chats2:
            num = 0
            for m in c.messages.all():
                if not m.is_read:
                    num += 1
            msg_read.append({
                "id":c.sender.id,
                "num":num
            })

        return Response({"sne":sne,"msg_read":msg_read})
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
def getMessagesChatsFree(request):
    client = RegisterFreelancer.objects.filter(id=request.data['id']).first()
    if client:
        chats = ChatMessageClient.objects.filter(receiver=client)
        sne=[]
        msg_read = []
        for c in chats:
            num=0
            for m in c.messages.all():
                if not m.is_read:
                    num+=1
            msg_read.append({
                "id": c.sender.id,
                "num": num
            })
            sne.append(UserSerializer(c.sender).data)
        return Response({"sne":sne,"msg_read":msg_read})
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)
@api_view(['POST'])
def active_client(request):
    client = RegisterUser.objects.filter(id=request.data['id']).first()
    if client:
        client.is_online=True
        client.save()
        return Response('ok')
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)
@api_view(['POST'])
def active_Free(request):
    client = RegisterFreelancer.objects.filter(id=request.data['id']).first()
    if client:
        client.is_online=True
        client.save()
        return Response('ok')
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)
@api_view(['POST'])
def de_active_client(request):
    client = RegisterUser.objects.filter(id=request.data['id']).first()
    if client:
        client.is_online=False
        client.save()
        return Response('ok')
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)
@api_view(['POST'])
def de_active_Free(request):
    client = RegisterFreelancer.objects.filter(id=request.data['id']).first()
    if client:
        client.is_online=False
        client.save()
        return Response('ok')
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)
@api_view(['POST'])
def getUnreadMessagesClient(request):
    user=RegisterUser.objects.filter(id=request.data['id']).first()
    if user:
        chat= ChatMessageFree.objects.filter(receiver=user)
        nums=0
        for c in chat:
            for m in c.messages.all():
                if not m.is_read:
                    nums+=1
        return Response(nums)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)
@api_view(['POST'])
def getUnreadMessagesFree(request):
    user=RegisterFreelancer.objects.filter(id=request.data['id']).first()
    if user:
        chat= ChatMessageClient.objects.filter(receiver=user)
        nums=0
        for c in chat:
            for m in c.messages.all():
                if not m.is_read:
                    nums+=1
        return Response(nums)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)
@api_view(['POST'])
def checkChatBegin(request):
    client = RegisterUser.objects.filter(id=request.data['client']).first()
    free =RegisterFreelancer.objects.filter(id=request.data['free']).first()
    if client and free:
       res= ChatMessageClient.objects.filter(sender=client,receiver=free).first()
       return Response(True if res else False)

    else:
        return Response(status=status.HTTP_404_NOT_FOUND)