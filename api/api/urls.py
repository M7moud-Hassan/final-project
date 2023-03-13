
from django.contrib import admin
from django.urls import path,include

from authentication.views import resetPasswordView, emailResetPassword


urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/',include('authentication.urls')),

]
