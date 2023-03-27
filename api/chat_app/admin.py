from django.contrib import admin

from chat_app.models import *

# Register your models here.
admin.site.register(ChatMessage)
admin.site.register(ChatMessageClient)
admin.site.register(ChatMessageFree)