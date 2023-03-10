
from django.contrib import admin

from django.urls import path, include

from django.urls import path,include

from authentication.views import resetPasswordView, emailResetPassword

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/',include('authentication.urls')),
<<<<<<< HEAD
=======
    path('reset_password/<uidb64>/<token>/', resetPasswordView, name='reset_password'),
    path('email_reset_password/', emailResetPassword, name='email_reset_password'),
>>>>>>> 75095bc431a238c6b7acf0325488c94b32ff08ba

]
