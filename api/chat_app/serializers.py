from rest_framework import serializers

from chat_app.models import ChatMessage, ChatMessageClient, ChatMessageFree



class ChatMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChatMessage
        fields = '__all__'


class ChatMessageClientSerializer(serializers.ModelSerializer):
    messages = ChatMessageSerializer(read_only=True, many=True)

    class Meta:
        model = ChatMessageClient
        fields = '__all__'


class ChatMessageFreeSerializer(serializers.ModelSerializer):
    messages = ChatMessageSerializer(read_only=True, many=True)

    class Meta:
        model = ChatMessageFree
        fields = '__all__'


