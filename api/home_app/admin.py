from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Job)
admin.site.register(JobImages)
admin.site.register(DisLike)
admin.site.register(LikeJob)
admin.site.register(notificationsClient)
admin.site.register(SendApply)
admin.site.register(ImagesSendApply)