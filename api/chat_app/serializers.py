from rest_framework import serializers

from chat_app.models import ChatMessage, ChatMessageClient, ChatMessageFree
from .models import RegisterFreelancer, RegisterUser


class ChatMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChatMessage
        fields = '__all__'


class ChatMessageClientSerializer(serializers.ModelSerializer):
    messages = ChatMessageSerializer(read_only=True, many=True)

    class Meta:
        model = ChatMessageClient
        fields = ['messages']


class ChatMessageFreeSerializer(serializers.ModelSerializer):
    messages = ChatMessageSerializer(read_only=True, many=True)

    class Meta:
        model = ChatMessageFree
        fields = ['messages']
class FreeLancerSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegisterFreelancer
        fields = ['id','first_name','last_name','user_image','is_online']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegisterUser
        fields = ['id','fname','lname','image','is_online']