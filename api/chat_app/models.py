from datetime import datetime

from django.db import models

from authentication.models import RegisterUser, RegisterFreelancer


class ChatMessage(models.Model):
    id = models.AutoField
    client=models.BooleanField(default=False)
    free=models.BooleanField(default=False)
    message = models.CharField(max_length=5000)
    create_at = models.DateTimeField(default=datetime.now())
    is_read = models.BooleanField(default=False)


# Create your models here.
class ChatMessageClient(models.Model):
    id = models.AutoField
    messages=models.ManyToManyField(ChatMessage,blank=True)
    sender = models.ForeignKey(RegisterUser, on_delete=models.CASCADE)
    receiver = models.ForeignKey(RegisterFreelancer, on_delete=models.CASCADE)


class ChatMessageFree(models.Model):
    id = models.AutoField
    messages = models.ManyToManyField(ChatMessage, blank=True)
    sender = models.ForeignKey(RegisterFreelancer, on_delete=models.CASCADE)
    receiver = models.ForeignKey(RegisterUser, on_delete=models.CASCADE)
    is_online = models.BooleanField(default=False)