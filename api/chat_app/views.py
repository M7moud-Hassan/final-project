from django.shortcuts import render
from requests import Response
from rest_framework import status
from rest_framework.decorators import api_view

from models import RegisterFreelancer, RegisterUser, ChatMessageClient
from serializers import ChatMessageClientSerializer


# Create your views here.

@api_view(['POST'])
def getMessagesClent(request):
    free=RegisterFreelancer.objects.filter(id=request.data['free']).first()
    client = RegisterUser.objects.filter(id=request.data['client']).first()
    if free and client:
        chats =ChatMessageClient.objects.filter(receiver=free,sender=client).first()
        return Response(ChatMessageClientSerializer(chats,many=True).data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
def getMessagesFree(request):
    free=RegisterFreelancer.objects.filter(id=request.data['free']).first()
    client = RegisterUser.objects.filter(id=request.data['client']).first()
    if free and client:
        chats =ChatMessageClient.objects.filter(sender=free,receiver=client).first()
        return Response(ChatMessageClientSerializer(chats,many=True).data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

